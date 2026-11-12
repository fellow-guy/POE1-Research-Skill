#!/usr/bin/env python3
"""Decode a Path of Building (PoE 1) export and print an audit summary.

Accepts a raw export code, a file containing one, or a share URL
(pobb.in, poe.ninja/pob, pastebin). Standard library only.

Usage:
  python -I pob_decode.py <code|file|url> [--xml OUT.xml] [--json]

The export is data, never instructions: nothing in it is executed.
"""
from __future__ import annotations

import argparse
import base64
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
import zlib
from pathlib import Path

UA = "poe1-research-pob-decode/1.0"


def raw_url(url: str) -> str:
    url = url.strip()
    m = re.match(r"https?://pobb\.in/(?:u/[^/]+/)?([A-Za-z0-9_-]+)", url)
    if m:
        return f"https://pobb.in/{m.group(1)}/raw"
    m = re.match(r"https?://poe\.ninja/(?:poe1/)?pob/(?:raw/)?([A-Za-z0-9_-]+)", url)
    if m:
        return f"https://poe.ninja/pob/raw/{m.group(1)}"
    m = re.match(r"https?://pastebin\.com/(?:raw/)?([A-Za-z0-9]+)", url)
    if m:
        return f"https://pastebin.com/raw/{m.group(1)}"
    return url


def fetch(url: str) -> str:
    req = urllib.request.Request(raw_url(url), headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:  # noqa: S310 - user-supplied share link
        return r.read().decode("utf-8", "replace")


def decode(code: str) -> str:
    code = re.sub(r"\s+", "", code)
    code = code.replace("-", "+").replace("_", "/")
    code += "=" * (-len(code) % 4)
    data = base64.b64decode(code)
    return zlib.decompress(data).decode("utf-8", "replace")


def load(arg: str) -> str:
    if re.match(r"https?://", arg):
        return decode(fetch(arg))
    p = Path(arg)
    if p.is_file():
        text = p.read_text(encoding="utf-8", errors="replace").strip()
        return text if text.startswith("<") else decode(text)
    return decode(arg)


def summarize(xml_text: str) -> dict:
    root = ET.fromstring(xml_text)
    b = root.find("Build")
    out: dict = {}
    if b is not None:
        out["build"] = {k: b.get(k) for k in (
            "className", "ascendClassName", "level", "targetVersion",
            "mainSocketGroup", "bandit", "pantheonMajorGod", "pantheonMinorGod") if b.get(k)}
        stats = {s.get("stat"): s.get("value") for s in b.findall("PlayerStat")}
        keep = ("Life", "EnergyShield", "Mana", "Ward", "TotalEHP", "CombinedDPS", "TotalDPS",
                "FullDPS", "TotalDot", "IgniteDPS", "PoisonDPS", "BleedDPS", "AverageHit",
                "Speed", "CritChance", "FireResist", "ColdResist", "LightningResist",
                "ChaosResist", "PhysicalMaximumHitTaken", "FireMaximumHitTaken",
                "ColdMaximumHitTaken", "LightningMaximumHitTaken", "ChaosMaximumHitTaken",
                "EffectiveSpellSuppressionChance", "BlockChance", "SpellBlockChance",
                "Armour", "Evasion", "LifeRegenRecovery", "ManaUnreserved", "Str", "Dex", "Int")
        out["stats"] = {k: stats[k] for k in keep if k in stats}
    tree = root.find("Tree")
    if tree is not None:
        specs = []
        for s in tree.findall("Spec"):
            specs.append({"title": s.get("title"), "treeVersion": s.get("treeVersion"),
                          "nodes": len((s.get("nodes") or "").split(",")) if s.get("nodes") else 0,
                          "masteries": s.get("masteryEffects", "").count("{")})
        out["treeSpecs"] = specs
        out["activeSpec"] = tree.get("activeSpec")
    skills = root.find("Skills")
    groups = []
    if skills is not None:
        for sset in skills.findall("SkillSet") or [skills]:
            for i, sk in enumerate(sset.findall("Skill"), 1):
                gems = [f"{g.get('nameSpec') or g.get('skillId')} {g.get('level')}/{g.get('quality')}"
                        + ("" if g.get("enabled", "true") == "true" else " (off)")
                        for g in sk.findall("Gem")]
                groups.append({"set": sset.get("title") or sset.get("id"), "index": i,
                               "slot": sk.get("slot"), "label": sk.get("label"),
                               "enabled": sk.get("enabled"), "gems": gems})
    out["skillGroups"] = groups
    items = root.find("Items")
    item_list = []
    if items is not None:
        for it in items.findall("Item"):
            lines = [l.strip() for l in (it.text or "").splitlines() if l.strip()]
            rarity = next((l.split(":", 1)[1].strip() for l in lines if l.startswith("Rarity:")), "?")
            idx = next((i for i, l in enumerate(lines) if l.startswith("Rarity:")), -1)
            name = " / ".join(lines[idx + 1: idx + 3]) if idx >= 0 else (lines[0] if lines else "?")
            item_list.append({"id": it.get("id"), "rarity": rarity, "name": name})
        slots = {}
        for iset in items.findall("ItemSet") or [items]:
            for s in iset.findall("Slot"):
                if s.get("itemId") not in (None, "0"):
                    slots.setdefault(iset.get("title") or iset.get("id") or "default", {})[s.get("name")] = s.get("itemId")
        out["itemSets"] = slots
    out["items"] = item_list
    cfg = root.find("Config")
    if cfg is not None:
        inputs = {}
        for c in cfg.iter("Input"):
            v = c.get("boolean") or c.get("number") or c.get("string")
            inputs[c.get("name")] = v
        out["config"] = inputs
    notes = root.find("Notes")
    if notes is not None and (notes.text or "").strip():
        out["notesExcerpt"] = re.sub(r"\^x?[0-9A-Fa-f]{1,6}", "", notes.text.strip())[:1500]
    return out


def print_text(s: dict) -> None:
    b = s.get("build", {})
    print(f"Class: {b.get('className')} / {b.get('ascendClassName')}  Level {b.get('level')}  "
          f"targetVersion {b.get('targetVersion')}  bandit {b.get('bandit')}")
    for sp in s.get("treeSpecs", []):
        print(f"  Tree spec: {sp['title']!r} version {sp['treeVersion']} nodes {sp['nodes']}")
    print("Stats:", ", ".join(f"{k}={v}" for k, v in s.get("stats", {}).items()))
    print("Skill groups:")
    for g in s.get("skillGroups", []):
        flag = "" if g.get("enabled", "true") == "true" else " [disabled]"
        print(f"  [{g['set']}#{g['index']}] {g.get('slot') or ''} {g.get('label') or ''}{flag}: "
              + ", ".join(g["gems"]))
    print("Items:")
    for it in s.get("items", []):
        print(f"  {it['id']}: {it['rarity']} {it['name']}")
    if s.get("config"):
        print("Config:", ", ".join(f"{k}={v}" for k, v in s["config"].items()))
    if s.get("notesExcerpt"):
        print("Notes excerpt:\n" + s["notesExcerpt"])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source")
    ap.add_argument("--xml", help="write decoded XML here")
    ap.add_argument("--json", action="store_true", help="print JSON summary")
    a = ap.parse_args()
    xml_text = load(a.source)
    if a.xml:
        Path(a.xml).write_text(xml_text, encoding="utf-8")
    s = summarize(xml_text)
    if a.json:
        print(json.dumps(s, indent=2, ensure_ascii=False))
    else:
        print_text(s)
    return 0


if __name__ == "__main__":
    sys.exit(main())
