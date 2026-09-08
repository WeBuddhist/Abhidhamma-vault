# Vibhaṅga root-to-commentary transclusion project — consolidated report

This is the single reference record for the whole project: linking root text `1-SOURCES/Text/pi-2.md` (18 chapters of the Vibhaṅga) into the commentary `pi-vibhanga-mulatiika.md` via Obsidian block-transclusion (`![[1-SOURCES/Text/pi-2.md#^2-N]]`). It replaces the seven separate phase reports that used to live in this folder.

## Current state

`pi-vibhanga-mulatiika.md` (the file at that name today) carries **255 transclusion links**, independently verified chapter by chapter, audited a second time from scratch, cross-checked against a pre-existing sibling file, and adjudicated link-by-link wherever the two disagreed. Whole-file structural sanity check: 0 malformed links, 0 dangling targets, 0 accidental back-to-back duplicates.

The **original pre-existing file** that used to occupy this name — an independently-built file this project did not create — is preserved as `pi-vibhanga-mulatiika.OLD.md`, kept for reference since it links a small number of items (`^2-763`, `^2-974`, `^2-976`, and a handful of style/granularity variants) that the current file doesn't, on weaker but not zero evidence.

## How the project got here

**1. Initial pass (18 chapters, 235 links).** Every chapter was linked using RUN-coverage methodology: a link's coverage spans from itself to the next link in root reading order, so every root item is accounted for as either a link or an explicit, justified gap — never silently skipped. Self-citations in the commentary (the text quoting the root's own "vibha. NNN" numbering) served as high-confidence confirmation wherever present. Anchor uniqueness (`text.count(anchor) == 1`) was verified before every insertion. Final count: 235 links across 18 chapters, from Maggaṅgavibhaṅgo's single link to Khuddakavatthuvibhaṅgo's 59.

**2. Independent audit.** The whole file was re-derived from scratch a second time — reading root and commentary fresh, not starting from the existing links — and diffed against what was actually there. This found 9 mismatched targets, 3 misplacements, 2 missing re-anchors, 16 genuine gaps, and 7 items flagged ambiguous (no confident single answer even on a fresh read), concentrated almost entirely in Chapters 12 and 17.

**3. Fixes applied (235 → 253 links, 33 edits across 7 chapters).** All concrete, non-ambiguous audit findings were corrected. The 7 ambiguous items were left as documented open questions, per the audit's own recommendation.

Mid-fix, close re-reading of Chapter 17 turned up something both the original pass and the audit had missed: root `pi-2.md` uses **two independent marker schemes** in Chapter 17's Tika-through-Sattaka combinatorial stretch — ordinary `^2-N` digit markers, and a second sequential scheme, `^2-U1`–`^2-U72`. A digit-only search silently skips every `^2-U#` marker, which had made several genuinely distinct root items look like they shared a marker with a neighbor. Once re-scanned with a pattern covering both schemes, several Chapter 17 fixes turned out to need retargeting to a specific `U`-marker (20 edits in that chapter alone, 242 → 253 links).

**4. Comparison against the pre-existing sibling file** (then `pi-vibhanga-mulatiika.md`, now `.OLD.md`, 277 links). The two files share identical base prose (confirmed by stripping all links from both and diffing what's left). Headline numbers: 201 root IDs linked in both; 76 linked only in the sibling file; 43 linked only in this project's file; the sibling file also carried 9 legitimate multi-link REOPENs and 2 dangling links with no matching root anchor (self-documented in its own text as a root-numbering gap).

**5. Adjudication of all 119 non-shared links.** Rather than leave "only in one file" as an unresolved list, every one of the 119 differing links was checked against the root text. The strongest evidence came from 22 cases where the *same* commentary sentence was anchored to *different* root IDs in each file — the sentence's own wording settles which is right. Result: this project's file was correct or more precise in 20 of 22 direct pairs, tied in 1, genuinely unresolved in 1. The single clearest pattern: the sibling file has the *same* `^2-U#` blind spot this project's file had before its own mid-fix discovery, and never corrected it — 6 separate Chapter 17 links land on the wrong digit marker for exactly that reason. Beyond the direct pairs, the sibling file's 6 other "clearly wrong" links and 2 dangling links were confirmed as genuine errors this project's file doesn't share; its remaining extra links were either style/granularity choices (linking individual repetitions this project treats as one RUN) or unconfirmed matches.

**6. Final gap-fills (253 → 255 links).** Of the sibling file's links that looked like genuine gaps in this project's file, two held up on close re-reading and were added: `^2-181` (kāma/byāpāda/vihiṃsā gloss, Dhātuvibhaṅgo) and `^2-802` (catasso paṭipadā / cattāri ārammaṇāni gloss, Ñāṇavibhaṅgo). Three more candidates (`^2-763`, `^2-974`, `^2-976`) were reconsidered and left out — weaker matches than first assessed, not confirmed enough to add. Two disputed placements (`^2-719`/`^2-720`, `^2-746`/`^2-732`) were left as-is: one low-stakes, one genuinely unresolvable from context alone.

**7. File promoted.** The old file at `pi-vibhanga-mulatiika.md` was renamed to `pi-vibhanga-mulatiika.OLD.md`, and this project's fully-verified file (previously `-fixed.md`) was renamed to take over the canonical `pi-vibhanga-mulatiika.md` name.

## What's still open

Two categories of loose ends, kept here rather than force-resolved:

- **7 ambiguous items** from the original audit (Ch1's Abhidhammabhājanīya stretch, Ch9's Rathadhura block, Ch16's post-`^2-796` block, and 4 in Ch17) where even independent re-derivation couldn't settle a single confident target.
- **`^2-746`/`^2-732`** (Paṭisambhidāvibhaṅgo) — the one genuinely unresolved disagreement between this file and `.OLD.md`; root content differs substantially at both candidate positions.
- **3 declined candidates** from `.OLD.md` (`^2-763`, `^2-974`, `^2-976`) that are plausible but not confirmed — worth a closer look if anyone wants to push adjudication further.

## Link-count progression

| Stage | Total links | Change |
|---|---:|---|
| Initial 18-chapter pass | 235 | — |
| After independent-audit fixes (33 edits, 7 chapters) | 253 | +18 net (retargets/removal/additions; largest single block was Ch17's 20-edit pass, +11 net, which is also where the `^2-U#` marker scheme was discovered) |
| After adjudication gap-fills (`^2-181`, `^2-802`) | **255** | +2 |

Density is very uneven across the text — from Maggaṅgavibhaṅgo's 1–2 links to Khuddakavatthuvibhaṅgo's ~70, which is also where nearly all of the audit's real errors and the adjudication's contested cases clustered, consistent with it being the largest chapter by a wide margin (226 root headings) and the densest combinatorial material in the whole Vibhaṅga.
