# Core mechanics quick reference (PoE 1)

Values marked **[PoB]** come from Path of Building Community source (`src/Data/Misc.lua`, `src/Modules/Data.lua`, `src/Modules/CalcDefence.lua`), snapshot `a69391d` (2026-11-10). They reflect PoB's model of the game. Re-grep before quoting a value after a major patch, since GGG changes these numbers. Unmarked statements are long-standing rules. Confirm any edge case against current patch notes or PoB code.

## Damage calculation order (hits)

1. **Base damage**: the skill's base, or weapon damage × attack Damage Effectiveness. Flat added damage is scaled by **Added Damage Effectiveness** (for example, Winter Orb's is 70% in 3.30).
2. **Conversion**: skill-intrinsic conversion applies first, then other conversion. Physical → Lightning → Cold → Fire → Chaos, one direction only. If global conversion totals more than 100%, it is scaled down to 100%. "Gain X% as extra" adds damage on top without removing the original.
3. **Increased/reduced**: all applicable `increased` modifiers are summed into one multiplier. Converted damage benefits from modifiers for every type it passed through. Example: phys converted to cold benefits from both phys and cold `increased`.
4. **More/less**: each `more` or `less` modifier multiplies separately. Supports, ascendancies and keystones are usually `more`.
5. **Critical strikes**: base player crit multiplier is +150% **[PoB]**. Crits add +50% to ailment DoT multiplier for ailments from crits **[PoB]**. Monsters have a 130% base multiplier and +30% crit ailment DoT multiplier **[PoB]**.
6. **Enemy mitigation**: armour applies to physical hits, resistances to elemental and chaos.
   - **Penetration** works only against hits. Exposure and curses lower resistance for everything.
   - Enemy maximum resistance is 75% **[PoB]**; enemy physical damage reduction is capped at 75% **[PoB]**.
7. **Damage-taken modifiers**: shock, Wither, "increased damage taken" and similar effects multiply the result.

Damage over time ignores conversion timing, crit multiplier (except the crit ailment DoT bonus) and penetration. It is scaled by `increased` and `more` modifiers plus **DoT multipliers**. Generic "damage" modifiers apply to both hits and DoT. "Hit damage" or "attack damage" modifiers do not apply to ailments unless they are ailment-specific.

## Damaging ailments [PoB]

| Ailment | Source damage | Base DoT | Base duration | Stacking |
| --- | --- | --- | --- | --- |
| Ignite | fire (by default) | 90% of hit damage per second | 4 s | Only the strongest ignite applies unless something lets ignites stack |
| Poison | physical + chaos | 30% per second | 2 s | Unlimited stacks |
| Bleed | physical | 70% per second | 5 s | Strongest applies unless Crimson Dance; moving enemies take more |

Monsters' ailments hit players with large `less` multipliers: ignite −72%, bleed −86%, poison −50% **[PoB `monsterConstants`]**.

## Non-damaging ailments [PoB `data.nonDamagingAilment`]

| Ailment | Default | Minimum | Maximum | Base duration |
| --- | --- | --- | --- | --- |
| Chill (less action speed) | 10% | 5% | 30% | 2 s |
| Shock (increased damage taken) | 15% | 5% | 50% | 2 s |
| Freeze | — | 0.3 s | 3 s | — |
| Scorch (−elemental resistance) | 10% | — | 30% | 4 s |
| Brittle (+base crit chance against) | 2% | — | 6% | 4 s |
| Sap (less damage dealt) | 6% | — | 20% | 4 s |

Ailment magnitude scales with the hit's damage of the associated type relative to the target's **ailment threshold**. Bosses have high thresholds, so shock and chill against them come mostly from "always shock" effects, effect modifiers or minimum-effect sources.

## Player defenses [PoB]

- **Resistances**: base maximum 75%; hard cap 90%; floor −200%.
  - Campaign penalty is −30% after Act 5 and −60% after Act 10. PoB's default config assumes −60%.
  - Since 3.30, mercenaries have their own resistance penalty by area level (see the 3.30 digest).
- **Armour**: damage reduction = Armour / (Armour + 5 × hit damage), capped at 90% for players. Armour is weak against large hits: 10,000 armour stops about 66% of a 1,000 hit but only about 17% of a 10,000 hit.
- **Evasion**: chance to be hit = 1.25 × Accuracy / (Accuracy + (Evasion/5)^0.9), clamped between 5% and 100%. Evade chance cap is 95%. Evasion uses an entropy system, so outcomes are less random than the percentage suggests.
- **Block**: attack and spell block caps are 75% (90% with maximum block modifiers).
- **Spell suppression**: chance cap 100%; base effect prevents 40% of suppressed spell damage.
- **Endurance charges**: each gives 4% physical damage reduction and 4% elemental damage reduction. Base maximum is 3 for endurance, frenzy and power charges.
- **Frenzy charges**: each gives 4% attack and cast speed and 4% more damage.
- **Power charges**: each gives +50% increased critical strike chance.
- **Fortification**: each stack gives 1% less hit damage taken; base maximum 20.
- **Energy shield**: recharge begins after 2 s and restores 33.3% of maximum ES per second (2000%/min). Ward recharge delay is 2 s.
- **Leech**: base rate 2% of maximum per second per instance. Maximum total rate is 20% of maximum life or mana per second (1200%/min) and 10% for ES. Each leech instance is capped at 10% of the maximum pool.
- **Mana**: base regeneration is 1.75% of maximum mana per second (105%/min).
- **Avoidance** of damage types caps at 75%.
- **Monster accuracy** grows steeply with level. See `data.monsterAccuracyTable` to estimate evade chance at a given area level.

eHP, maximum hit and recovery answer different questions. A build is safe only if it handles one-shots (maximum hit by damage type), sustained damage (recovery against incoming DPS), ailments (freeze, stun, corrupted blood, reflect-style map modifiers) and degens.

## Player and enemy constants [PoB]

- Life: +12 per level. Mana: +6 per level. Accuracy: +2 per level.
- Base movement speed constant is 37. Dual-wielding adds 10% more attack speed and 20% block chance.
- Base limits: totems 1; traps 15; remote mines 15; sigils (brands) 3; maximum rage 30.
- Impale: 8 s duration, 5 reflected hits; each impale stores 10% of the hit.
- Experience penalty: area level above 70 lowers effective monster level for XP. Higher-level characters lose XP faster if the area level is far below their own level.
- PoB enemy presets:
  - Standard boss: level 83, default chaos resistance 25%.
  - Pinnacle boss: level 84, 50% elemental and 30% chaos resistance; penetration placeholder `pinnacleBossPen`.
  - Uber pinnacle boss: level 85, adds 70% less damage taken.
  - Read `src/Modules/ConfigOptions.lua` (`enemyIsBoss`) for current armour, evasion and damage assumptions.
- Monster life by level, map-level life multipliers and boss life multipliers are tabulated in `src/Data/Misc.lua` (`monsterLifeTable`, `mapLevelLifeMult`, `mapLevelBossLifeMult`). Use them for "how much tankier are T16/T17 monsters" questions.

## Skill and support mechanics

- **Transfigured gems** keep the base gem's tags and level progression but change behaviour. They come from Divine Fonts (Labyrinth) and drops. PoB's Transfiguration constant is 0.3; check `Gems.lua` for each variant.
- **Exceptional supports** (Empower, Enlighten, Enhance, Awakened gems, and newer exceptional gems such as Transfusion) are not normal drops. Check source tables before assuming access in SSF.
- **Triggers** (Cast on Crit, Cast while Channelling, CWDT, Mjolner, Arcanist Brand, Spellslinger and similar) have cooldowns and cost or reservation rules. PoB `CalcTriggers.lua` models trigger rates and caps; read it before trusting a trigger build's DPS.
- **Reservation**: auras and heralds reserve mana or life by percentage. Reservation efficiency is not the same as reduced reservation; check how PoB combines them.
- **Minions** use their own stat blocks (`src/Data/Minions.lua`, `Spectres.lua`). "Minion damage" scales minion hits and DoTs; player "damage" modifiers do not, unless a specific mechanic says otherwise.
- **Totems, traps, mines and brands** have placement or throw speed and can carry `more` modifiers from their supports. Totems scale with "totem" and "attack/spell" modifiers. In 3.30, the Artillery Quiver implicit adds +1 attack totem.
- **Accuracy**: attacks can miss; spells cannot. Resolute Technique removes misses but also removes crits.

## Keyword lookups

When a question involves a keyword, keystone or "nearby" range, prefer the in-game keyword text, which 3.30 expanded, plus PoB's `ModParser.lua` match patterns and `Data/StatDescriptions`. "Nearby" ranges were added to many descriptions in 3.30 without changing them. Older PoB or wiki pages may lack the metre values.
