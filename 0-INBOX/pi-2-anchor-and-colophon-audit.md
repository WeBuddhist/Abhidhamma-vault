---
title: "pi-2.md — anchor and colophon audit"
date: 2026-09-09
status: report
scope: "Book II (Vibhaṅga), 1-SOURCES/Text/pi-2.md and 3-TRANSFORMATIONS/Plans/Daily-Tipitaka/en/schedule.md"
raised_by: "daily-tipitaka-day batch for days 122–127"
---

# pi-2.md — anchor and colophon audit

Three things turned up while checking chapter boundaries for days 122–127. One was fixed in the same pass; two are open. Nothing in `1-SOURCES/` was changed — items 1 and 2 are reports, not repairs.

A note on method, because a first pass got two of these wrong. The schedule's verse column contains **single-verse rows** (`| day-093 | … | 153 |`) as well as ranges, and Book I day rows carry verse numbers that overlap Book II's. A parser that only matches `N–M`, or that does not scope to day rows 78–173, produces false gaps and false mismatches. The numbers below come from a parser that handles both.

## 1. The 2026-08-24 source repair has been reverted — OPEN

On 2026-08-24, four uddesa lines that had lost their anchors and been absorbed into neighbouring blocks were split back out on Evan's authorisation: `^2-185`, `^2-252`, `^2-264`, `^2-298`. Days 106–118 each carry a `source_repair` frontmatter note recording it, ending *"Both files now carry 1045 anchors, ^2-0 – ^2-1044, no gaps or duplicates."*

**That is no longer true of this working copy.**

| File | Anchors | Missing |
|---|---:|---|
| `1-SOURCES/Text/pi-2.md` | 1041 | `^2-185`, `^2-252`, `^2-264`, `^2-298` |
| `…/en-Contemporary-English-Abhidhamma/pi-2-english-plain-zeroshot.md` | 1041 | same four |
| `AI_translation/english/pi-2-english-plain-zeroshot.md` | 1041 | same four |

Exactly the four the repair restored, gone from all three files. The likely cause is commit `a5612ed` — *"Update block id's and upload root-text and it's translation"* — which re-uploaded the root text and the translation after the repair commit. Whoever re-uploaded almost certainly did not know the repair was in there.

**What it actually breaks.** Two of the four sit inside already-drafted day ranges:

| Day | Scheduled range | Missing verse | Effect |
|---|---|---|---|
| day-108 | 249–255 | `^2-252` | interior verse — not a §4/§6 boundary entry |
| day-114 | 293–305 | `^2-298` | interior verse — not a §4/§6 boundary entry |

Because both are interior, neither day file prints a broken entry, which is why this went unnoticed. The app will pull one verse fewer than the range implies for each of those two days. `^2-185` and `^2-264` were never inside any scheduled range — the schedule was built against the unrepaired text — so their loss changes nothing downstream.

Each of days 106–118 has had a dated correction appended to its `source_repair` note rather than having the original claim deleted, so the history stays readable.

**Suggested fix.** Re-apply the 2026-08-24 split to `pi-2.md` and both translation copies, then protect it — either by making the upload pipeline preserve local anchor edits, or by keeping the four splits as a patch re-applied after every upload. Re-applying edits `1-SOURCES/`, so it needs Evan's explicit go-ahead.

## 2. One chapter colophon is in no scheduled day — OPEN

`^2-831` is the closing block of chapter 16, `Ñāṇavibhaṅgo` — its last line is `Ñāṇavibhaṅgo niṭṭhito.` It falls between two scheduled days and belongs to neither:

| Day | Range |
|---|---|
| day-152 | 816–830 |
| **— gap —** | **831** |
| day-153 | 832–849 |

It is the only verse in the whole of Book II present in the text but absent from the schedule. Nobody reading the plan reaches the end of chapter 16.

**Suggested fix.** Widen day-152 to 816–831, matching the pattern everywhere else (a chapter's colophon closes that chapter's last day). day-152 is scheduled for 12 October, so there is time. The same edit is needed in the source spreadsheet.

## 3. Two days straddled a chapter boundary — FIXED 2026-09-09

`^2-430` is the closing block of chapter 8 (`Sammappadhānavibhaṅgo niṭṭhito.`) and `^2-485` the closing block of chapter 10 (`Bojjhaṅgavibhaṅgo niṭṭhito.`), but both had been scheduled into the *following* chapter's first day. Corrected in `schedule.md` on Evan's direction:

| Day | Was | Now |
|---|---|---|
| day-123 | 413–429 | **413–430** |
| day-124 | 430–446 | **431–446** |
| day-127 | 475–484 | **475–485** |
| day-128 | 485–495 | **486–495** |

After the fix, all 18 Book II chapter boundaries check clean and no day spans two chapters. **The source spreadsheet — `0-INBOX/200 Days - ITCC_2026_Bodhgaya_Reading_Schedule - Day-by-Day.csv`, and the Google Sheet behind it — still carries the old split and needs these four edits.**

## Re-running these checks

Worth repeating after any re-upload of `pi-2.md`.

**Anchor census** — expect 1045 anchors, `^2-0` … `^2-1044`, no gaps:

```bash
python3 -c "
import re
t=open('1-SOURCES/Text/pi-2.md',encoding='utf-8').read()
ns=sorted(int(x) for x in re.findall(r'\^2-(\d+)\$', t, re.M))
print('count',len(ns),'missing',[n for n in range(max(ns)+1) if n not in set(ns)])
"
```

**Boundary and coverage check** — pairs each chapter's last anchor with the scheduled day containing it, and lists verses scheduled but absent, or present but unscheduled. The working script from this audit is kept at `4-SYSTEM/scripts/check-schedule-boundaries.py`. Two things it must get right, both of which caught out a first attempt: parse single-verse rows (`| 153 |`, no dash) as well as ranges, and scope to day rows 78–173 so Book I's overlapping verse numbers do not match.
