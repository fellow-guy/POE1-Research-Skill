---
name: poe1-research
description: All-purpose Path of Exile 1 knowledge and research. Use for any PoE 1 question - patch notes and league changes, mechanics and damage/defense math, skills, gems, uniques, crafting, Atlas and farming, campaign leveling, bosses, trade and prices, and reviewing or decoding Path of Building builds and league-start guides. Uses Path of Building Community data, PoEDB, official patches and creator guides. Distinguishes PoE 2 and Ruthless.
---

# Path of Exile 1 research

## Route the question

Load only the reference you need:

| Question | Reference |
| --- | --- |
| How a mechanic works, formulas, caps, ailments, defenses | [mechanics.md](references/mechanics.md) |
| Crafting methods, currency, vendor recipes, item tiers, trade valuation | [crafting-economy.md](references/crafting-economy.md) |
| Atlas, maps, Threads, bosses, farming strategy | [atlas-endgame.md](references/atlas-endgame.md) |
| Campaign, labs, quest points, leveling plan | [campaign-leveling.md](references/campaign-leveling.md) |
| Abbreviations, classes, ascendancies, league jargon | [glossary.md](references/glossary.md) |
| Which league or version introduced something; dates | [league-history.md](references/league-history.md) |
| Where to look up any data; source reliability and access limits | [sources.md](references/sources.md) |
| PoB cache, decoding exports, auditing calculations | [path-of-building.md](references/path-of-building.md) |
| Reviewing incoming league-start guides; candidate ledger format | [league-start.md](references/league-start.md) |

**Current-league material** (patch digest, candidate ledger, cache provenance) lives in the user's project, not in this skill. Look for `research/INDEX.md` in the current PoE 1 project. Read its patch digest before answering about the current league. If no digest exists, consult the official patch notes directly.

## Tools

- **Decode any PoB link or code**: `python -I scripts/pob_decode.py <url|code|file> [--xml out.xml] [--json]` (path relative to this skill's folder). Use this instead of reasoning from a pobb.in summary page.
- **Look up exact game data** in the local PoB clone (`.reference-cache/PathOfBuilding` in the project) with `rg` / Grep. Examples: gem stats in `src/Data/Skills/`, uniques in `src/Data/Uniques/`, mods in `src/Data/Mod*.lua`. Check the clone's commit and tree versions first; it can lag a new patch.
- **Web**: GGG forum, PoEDB, creator sites, pobb.in and poe.ninja are readable. PoE Wiki and YouTube usually block automated fetches; say so rather than guessing their content.

## Ground rules

1. **Establish the version and mode.** State the patch, the date of your information, and the assumed mode (softcore trade unless told otherwise). Note where SSF, Hardcore or Ruthless would change the answer. PoE 2 is a different game; never import its mechanics.
2. **Latest official change wins.** For any value that a patch may have touched, check the current digest or patch notes before quoting PoB, wiki or a guide. Read old patch notes only to trace a specific dependency.
3. **Label the evidence.** Separate "confirmed" (patch notes, game data), "modeled" (PoB), "reported" (creator, community) and "predicted" (your inference). Never claim to have watched a video or run PoB when you only read notes or stored stats.
4. **Numbers need a source.** Cite the file, URL or patch line for a constant, a price or a DPS figure. Do not invent prices, clear speeds, DPS or tier rankings. Prices are league- and time-specific.
5. **Follow dependencies.** A build depends on its ascendancy, supports, uniques, transfigured gems, league mechanics and crafting methods, not just its main skill. An unchanged gem does not mean an unchanged build.
6. **Defenses are multi-dimensional.** Report maximum hit, mitigation, avoidance, recovery and ailment handling separately. Do not call a build tanky from eHP alone.
7. **Give a recommendation.** For "what should I play or do" questions, recommend a small set fitted to the user's stated playstyle and content. For each, give the benefit, the main drawback, the key dependency, your confidence and a direct link.

## Evaluating a build or guide

- Decode the export. Check `targetVersion` and tree versions, the level of the "starter" spec, the leveling specs, and the config (enemy preset, charges, flasks, buffs, custom modifiers).
- Walk the progression: campaign skill → swap level → first maps (4–5 links, realistic rares) → upgrade order → endpoint.
- Check every patch change that touches its skills, supports, ascendancy notables, uniques and the crafts it needs.
- Use [league-start.md](references/league-start.md) for the full review loop and the ledger format.

## Explaining patch impact

Prioritize what changes the user's decisions: build choice, campaign preparation, gearing cost, Atlas strategy and farming. Separate confirmed mechanics from profit predictions. Recheck currency strategies whenever the Atlas or loot systems change, even when the build survives.

## Maintaining this skill

Keep durable knowledge here and volatile, league-specific material (digests, ledgers, prices) in the project's `research/` folder, dated. When a new patch lands:
1. Write `research/patch-<version>-digest.md` from the official notes.
2. Update the version-sensitive lines in `mechanics.md`, `crafting-economy.md`, `atlas-endgame.md` and `league-history.md`.
3. Refresh the PoB clone (`git pull --ff-only`) and re-grep the constants listed in `path-of-building.md`.

When this skill is shared between tools, keep one canonical checkout, such as `~/.agents/skills/poe1-research/`, with directory junctions or symlinks from `~/.claude/skills/poe1-research` and `~/.codex/skills/poe1-research`. Edit the canonical folder or its links. Preserve existing junctions so the tools continue using the same files.
