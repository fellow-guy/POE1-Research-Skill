# PoE 1 Research Skill

An all-purpose Path of Exile 1 research skill for Codex and Claude Code, covering game mechanics, crafting, campaign progression, Atlas farming, patch changes, and league-start build reviews.

## Contents

- `SKILL.md`: task routing, source verification, and research workflow.
- `references/`: mechanics, crafting/economy, Atlas/endgame, campaign, glossary, league history, sources, and build review guidance.
- `scripts/pob_decode.py`: standard-library Python helper for decoding Path of Building exports and inspecting stored configurations.

## Install

Clone into the skills directory for the tool you use:

```sh
# Codex
git clone https://github.com/fellow-guy/POE1-Research-Skill.git ~/.codex/skills/poe1-research

# Claude Code (alternative)
git clone https://github.com/fellow-guy/POE1-Research-Skill.git ~/.claude/skills/poe1-research
```

For a shared installation, clone once to `~/.agents/skills/poe1-research` and link your tools' skill directories to that checkout. Preserve existing installations and directory links. A private repository requires GitHub access.

## Use

Ask for a PoE 1 mechanics explanation, patch analysis, crafting plan, or league-start build review. In Codex, the skill can also be invoked as `$poe1-research`.

Decode a PoB from the repository root with Python 3.10 or newer:

```sh
python -I scripts/pob_decode.py https://pobb.in/BUILD_ID --json
```

Replace `BUILD_ID` with the creator's share code. The helper inspects the export; it does not run PoB's calculation engine.

## Data and updates

Game databases and creator guides are consulted live. The optional Path of Building Community cache is fetched separately and is not bundled. Keep league-specific digests, build ledgers, prices, and cache provenance in your PoE project's `research/` folder.

Check the target patch and source dates before relying on values. Cached PoB data and creator exports can lag a new release. Refreshing happens when requested; this repository does not run background monitoring.

This is an unofficial community research tool. Path of Exile and referenced third-party tools belong to their respective owners.
