# Crafting, items and economy (PoE 1)

Crafting changes almost every league. This file holds the stable framework plus the 3.30 changes known at the time of writing. Before giving a crafting recipe, check the current patch digest in the project's `research/` folder and Craft of Exile. An old guide's method can now fail or cost more.

## Item model

- **Rarity**: Normal, Magic (1 prefix + 1 suffix), Rare (up to 3 prefixes + 3 suffixes), Unique.
  - Jewels have 2 + 2 affixes.
  - Abyss jewels and cluster jewels have their own pools.
- **Item level** gates which modifier tiers can roll. Base type, influence (Shaper, Elder, Conquerors, Eldritch implicits) and tags decide the pool.
- **Implicits**: base implicits; corruption implicits; Eldritch implicits from Eater of Worlds and Searing Exarch (Embers/Ichors).
- **Fractured** modifiers are permanent. **Synthesised** items have special implicits. **Corrupted** items cannot be modified except by special currency, and "Twice Corrupted" now comes from altars, Lapidary Lens and Djinn-Touched Vaal Orbs.
- **Sockets and links**: Jeweller's (count), Fusing (links), Chromatic (colours). The bench offers set sockets, links and colours.
  - **3.30 change:** a new bench option sets all sockets white for an Orb of Scouring (plus a Vaal Orb if the item is corrupted).
- **Item Tiers (3.30, Act 6+)**: Rare and Magic drops can have Item Tier 2–5. Higher tiers raise modifier tiers, base type, quality, sockets and links. Monster rarity raises tier chance.
  - Tier 5 items can have +1 item level or drop Fractured Magic.
  - Some bases need minimum tiers: Stygian Vise needs Tier 5; Steel Ring needs Tier 3.
- **Modifier Tier Rating (3.30 rework)**: it no longer changes which modifier types appear. Each point raises tier smoothly, with no breakpoints.
  - Genesis tree small nodes give +10 (was +20).
  - Notables give 200% more chance (was 300%) or 50% less (was 60%).

## Methods (what each tool does)

| Method | Use | Notes |
| --- | --- | --- |
| Transmute/Alteration/Augment/Regal | Magic-base spamming, then Regal to rare | Cheap targeted base mods |
| Chaos / Alchemy / Scour | Reroll rares | Low control |
| Essences | Guarantee one modifier and reroll the rest | Essence of Trickery is new in 3.30 |
| Fossils + resonators (Delve) | Weighted rerolls | Delve Atlas cluster removed in 3.30; fossil supply may shift |
| Harvest (Horticrafting) | Reforge keeping prefixes/suffixes, add/remove by type, change resists or damage | 3.30: resist changes cost 300 Lifeforce of two colours; damage changes cost 300 of two colours plus Crystallised Rancour |
| Crafting bench | Add one crafted modifier; meta-crafts | 3.30: prefix/suffix lock costs by item type (below) |
| Eldritch currency | Implicits and influence-tier swaps | Exarch/Eater altars also drop Threads in 3.30 |
| Beastcrafting | Splitting, imprinting, flask modifiers and more | 3.30: yellow beasts gone; flask crafts need any Red Beast |
| Recombinator | Merge two items' modifiers | 3.30: result takes the chosen base's item level; not usable on corrupted items |
| Annulment | Remove a random modifier | 3.30: "Cannot roll Attack/Caster" meta-crafts no longer protect against annulment |
| Hinekora's Lock | Preview the next currency outcome | Mirror and Eternal no longer remove its effect |
| Fracturing Orb | Fracture one modifier | Fractured drops reduced in 3.30 |
| Gwennen (Expedition) | 3.30: "take a chance" for one Astragali — choose from three crafting-option pairs | No longer gambles items |
| Rog (Expedition) | Deal-based crafting | 3.30: rerolls are 1, 3 or 5 (was 3, 6, 10) |
| Vaal Orb / altars | Corruption outcomes | Altar of Corruption can destroy items; Lapidary Lens can destroy items |

### 3.30 bench meta-crafts

| Option | Cost |
| --- | --- |
| Lock 1 prefix or 1 suffix | 1 Divine |
| Lock 2 prefixes or 2 suffixes | 2 Divine |
| Lock all prefixes or suffixes — weapons | 4 Divine + 1 Sacred |
| Lock all prefixes or suffixes — armour and quivers | 4 Divine + 4 Blessed |
| Lock all prefixes or suffixes — jewellery | 4 Divine + 8 Exalted |

Crafting recipes no longer drop in Unique Maps. Meta-modifier recipes moved to Nightmare Maps.

## Currency and vendor recipes (3.30)

- **Drop pools follow monster rarity.** Scrolls drop only from Normal monsters. Transmutation, Alteration and Jeweller's need Magic. Alchemy, Chaos, Divine and Mirror need Rare. More item rarity gives better currency. This is the largest economy change since 3.0.
- **Item Quantity on maps is replaced by Atlas Drops.** It affects maps, Threads, monster-specific drops and league resources.
- **Orbs of Chance** are rarer and no longer sold by vendors, but have a much higher Unique chance.
- **Orbs of Binding** are removed; the Bestiary recipe now gives Orbs of Regret. Sacred Orbs and Alchemy are more common.
- **Vendor recipes**:
  - Two same-name rares give a Chaos Orb; three give an Exalted Orb. Quality no longer matters.
  - A full rare set with one item below level 60 gives Alchemy.
  - Gems at level 28–33 vendor for Alteration; 34–37 for Alchemy.
  - An Orb of Scouring costs 4 Fusing. Transmutation can be bought for one Augmentation.
  - Vaal Orb recipe: 5 Vaal gems.
- **Soul Cores** replace Coins of Knowledge, Power and Skill. New Soul Cores: Finesse, Instability, Intellect and Might.
- **Removed**: Scarabs (now Threads), Coins of Restoration and Desecration, Mortal and Sacrifice Fragments (Mortal converted to Royal Visage), Mirage Incubators, Veiled items outside Betrayal.

## Valuation and trade

- Use the [official trade site](https://www.pathofexile.com/trade) for listings and [poe.ninja](https://poe.ninja/) for currency and item index prices. Record league, platform, time and sample size.
- Asking prices are not sale prices. Early league, thin listings and price fixing make prices volatile. Never quote last league's prices for a new league.
- Divine Orb is the usual high-value unit; Chaos Orb is the trade small change. The Currency Exchange (Faustus) gives in-game ratios and a fee.
- Good starter planning lists the **first purchases that unlock the build**, such as a key unique, 5/6-link, gem or cluster. List those rather than a full endgame shopping list.

## Crafting feasibility checklist

1. Exact base, item level, influence or Eldritch state, and mode (trade or SSF).
2. Modifier pool with weights and groups (Craft of Exile; PoB `Data/Mod*.lua`; PoEDB).
3. Steps with expected cost and **variance**. Name the bad-outcome branch (bricking, annul hitting the wrong modifier, or destruction for altars and Lapidary Lens).
4. Verify each step against current mechanics. 3.30 changed locks, annul protection, recombinators, corruption, fractures and Rog.
5. Compare against buying the finished item.
