# PoE 1 source index

## Route the question

| Question | Start here | Cross-check / limitation |
| --- | --- | --- |
| Patch, hotfix, league announcement | [GGG patch forum](https://www.pathofexile.com/forum/view-forum/patch-notes), linked expansion and announcement posts | Distinguish announcements, final notes, later edits, normal game and Ruthless |
| Skill/support gem values, quality, tags, transfigured variants | [PoEDB](https://poedb.tw/us/), PoB `src/Data/Gems.lua` and `Skills/` | Exact gem name, level, quality and patch; do not treat tags as complete scaling rules |
| Bases, uniques, explicit/implicit mods, item levels, influence, mod groups and weights | PoEDB; PoB `Bases/`, `Uniques/`, `Mod*.lua` | Legacy items and unavailable league modifiers can remain in data |
| Damage and defense calculations, triggers, reservation and resource sustain | [PoB Community](https://github.com/PathOfBuildingCommunity/PathOfBuilding), actual creator export | Model assumptions are not game measurements; inspect unsupported effects and open calculation issues |
| Mechanics and historical interactions | [PoE Wiki](https://www.poewiki.net/), cited GGG explanations, relevant historical patches | Check revision/context; prefer this community wiki over abandoned Fandom pages |
| Monsters, spectres, minions, boss skills | PoEDB; PoB `Spectres.lua`, `Minions.lua`, `Bosses.lua`, `BossSkills.lua` | Datamined skill existence does not prove availability as a usable spectre |
| Passives, ascendancies, masteries, timeless/cluster jewels | PoB `TreeData/`, `ClusterJewels.lua`, `TimelessJewelData/`; [official tree](https://www.pathofexile.com/passive-skill-tree) | Verify tree version and special event variants; imported tree version may differ from current gem data |
| Crafting methods and probabilities | [Craft of Exile](https://www.craftofexile.com/), PoEDB, patch notes | Select PoE 1; use correct base, item level, tags, influence and restrictions. Expected cost is not guaranteed cost |
| Trade availability and price | [Official trade](https://www.pathofexile.com/trade), [poe.ninja](https://poe.ninja/) | Correct league/platform; asking prices are not completed sales; sparse listings and launch volatility matter |
| Build adoption and progression | poe.ninja builds with dated early-league snapshots | Sample/ladder selection and survivor bias; popularity does not measure reliability |
| Atlas and farming | [Official Atlas tree](https://www.pathofexile.com/atlas-skill-tree), patch notes, poe.ninja Atlas trees, original farming tests | Record map investment, sample size, time, sale assumptions and character capability |
| Loot filters and launch preparation | [FilterBlade](https://www.filterblade.xyz/), creator's published filter | Correct game/league; check required bases and campaign items before using strict filters |
| APIs and official data exports | [GGG developer documentation](https://www.pathofexile.com/developer/docs) | Follow documented endpoints, authentication and rate limits; do not guess undocumented API contracts |
| Fresh starter guides | Original creator sites, official forum build sections, creator YouTube channels, Mobalytics and PoE Vault author pages | Read actual content/date and PoB, not only a refreshed title |
| Bulk game data (gems, mods, bases, stat text) as JSON | [RePoE](https://github.com/repoe-fork/repoe) exports; [poe-tool-dev](https://github.com/poe-tool-dev) projects (`dat-schema`, ggpk tools) | Check export date and game version; community schemas can lag a patch |
| PoB share links | `pobb.in/<id>` → `pobb.in/<id>/raw`; `poe.ninja/pob/<id>` → `poe.ninja/pob/raw/<id>`; `pastebin.com/raw/<id>` | Decode with `scripts/pob_decode.py`. Verified working for pobb.in on 2026-11-12 |
| Character / ladder lookups | poe.ninja builds (filter by skill, item, ascendancy); official profile `pathofexile.com/account/view-profile/<name>` | Private profiles are inaccessible; do not guess |
| Leveling route, labs | [Exile Leveling](https://heartofphos.github.io/exile-leveling/), [poelab.com](https://www.poelab.com/) | Routes update for new campaign changes after launch |
| Price checking in-game | Awakened PoE Trade / Exiled Exchange (overlay tools) | Uses official trade; same caveats as trade |
| Atlas planning | Official Atlas tree page; poe.ninja Atlas tree stats; creator Atlas guides | 3.30 tree was fully rebuilt. Pre-3.30 Atlas trees do not apply |
| Discover additional candidates | [PoE Builds](https://www.poebuilds.cc/), [PoB Archives](https://pobarchives.com/), [PathOfExileBuilds](https://www.reddit.com/r/PathOfExileBuilds/) | Follow attribution back to author. Aggregator metrics and community claims need independent checks |

## Freshness and conflicts

For each consequential finding record URL or local source path, accessed date, game patch, source revision if available, claim, and confidence. Use small summaries rather than bulk copies of websites.

For current balance, start with the latest applicable official change. For implemented formulas, inspect the matching PoB code and data, then distinguish its model from observed game behavior. Databases may contain unreleased or legacy data; wiki articles and creator guides may lag. If sources conflict, name the discrepancy and leave that interaction unresolved until evidence settles it.

Recheck patch amendments, PoB releases and guide revisions during each pre-launch review. Recheck prices during the session in which a purchase recommendation is made. Preserve dated historical snapshots for comparisons rather than silently replacing them with current values.

Known access limits from this environment (2026-11-12): PoE Wiki (`poewiki.net`) serves an Anubis bot check to automated fetches, so use PoEDB or PoB source instead and tell the user when a wiki citation could not be read. YouTube pages and some news sites (Massively OP) return 403 or throttle. Creator sites, PoEDB, pobb.in, GGG forum and poe-vault were readable.

On inaccessible sources, try another public authoritative source or a targeted indexed result and disclose the gap. A blocked page is not evidence of its contents. Do not retry blocked endpoints repeatedly, bypass access controls, or claim videos were watched when only notes were available.

## Coverage boundaries

PoB covers a large model of builds, not every game mechanic, drop rate, private character, or creator export. Internet databases remain live references, not a complete offline mirror. Specific build links must still be retrieved. Broad coverage means consulting the appropriate sources, not claiming exhaustive review of all information.
