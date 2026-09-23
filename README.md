<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/hero.gif?v=3" width="100%"/>

<h1 align="center">volkansync</h1>
<p align="center"><sub>SYSTEMS · INFRASTRUCTURE · SECURITY AUTOMATION &nbsp;—&nbsp; ESKİŞEHİR, TR</sub></p>

<p align="center">
<a href="https://github.com/volkansync/field-notes"><img src="https://img.shields.io/badge/field--notes-casefiles-E6CC55?style=flat-square&labelColor=0E1628" /></a>
<a href="https://www.linkedin.com/in/volkan-%C3%A7evik-90b1a937a"><img src="https://img.shields.io/badge/LinkedIn-0E1628?style=flat-square&logo=linkedin&logoColor=E6CC55" /></a>
<a href="https://www.youtube.com/@volkansync"><img src="https://img.shields.io/badge/YouTube-0E1628?style=flat-square&logo=youtube&logoColor=E6CC55" /></a>
</p>

---

## I fix systems by finding out why they broke.

No degree, no early start, no one to ask — just a machine that kept failing and a
refusal to accept *"it works now"* as an explanation.

So most of what I do is elimination. A symptom, the explanations it **wasn't**, a
mechanism, a test that could have proved me wrong, and what the numbers actually said.
Sometimes they said I was wrong. Those are written down too.

---

## Casefiles

**Bluetooth audio dropping out** — one channel first, alternating, on two different headsets.
Not the headphones. Not the codec. Not *"just use 5 GHz."*
→ **2.4 GHz band contention**, amplified by Wi-Fi power saving.
`152.5 → 18.3` failures per day on the same network. Ten days at exactly zero.
And a second step no guide mentions: the Bluetooth link has to be renegotiated, or the fix looks like it didn't work.

**TLS certificate errors** — one service only, chain intact.
Not the clock. Not the CA bundle. Never the certificate.
→ **ISP-level DNS blocking.** The resolution path, not the crypto.

**Anti-cheat error 60099** — on an otherwise healthy install.
Not a reinstall. Not a prefix reset — those work once, then break again.
→ **`tr_TR` locale plus a missing Windows font.** Documented so it survives the next reset.

**Desktop shell dying after every upgrade** — reliably, monthly.
Not the package.
→ **Qt ABI break.** Found the recurring trigger instead of re-fixing the symptom.

<sub>Full writeups, the journal data, and the measurement code → **[field-notes](https://github.com/volkansync/field-notes)**</sub>

---

## Instruments

The fault is rarely the hard part. Building a measurement that doesn't lie is.

**`bt-dropout-test.sh`** — 2×2 harness. Pins the Wi-Fi band, toggles power saving, samples
xruns and signal per arm, restores every setting on exit including `Ctrl+C`.

**`analiz.py`** — kept in the repo *because it was wrong*. It normalised failures by
"Bluetooth-active hours," a denominator driven by the same failures as the numerator.
It hid the effect it was measuring, and finding that out took longer than finding the fault.

**`analiz3.py`** — the one that held. Per-day, per-network, with usage detected from events
that fire independently of errors — so "zero failures" could finally be told apart from "not used."

---

## Field

Arch on Wayland, daily. Comfortable in the parts that break: `systemd` units, NetworkManager,
the audio and display stacks, ABI breakage after upgrades. Reverse proxies, TLS, DNS resolution
paths, containerised services each with their own database.

Heading toward cloud administration and security automation.

**In training** — German → B1 *(daily)* · RHCSA or LFCS *(queued)* · CCNA *(queued)* · AZ-104 / AWS SAA *(queued)*

<sub>`queued` means queued. Not started, and not pretending otherwise.</sub>

---

<details>
<summary><b>Case log</b> — decisions that were expensive, kept even when they read badly later</summary>

<br/>

| | decision | why |
|---|---|---|
| `2026-09` | Closed the web agency; everything moved to one product | No revenue, and the fixed costs compounded monthly |
| `2026-09` | Nothing new starts until the current product ships | A scan across 18 categories found a maintained free competitor in **every one** |
| `2026-09` | Deterministic logic is the default; AI is an optional layer | When the API credit runs out, the product still has to work |
| `2026-09` | One repo, one deployment, one database per product | A failure in one must not take down another |
| `2026-07` | Wayfire over Hyprland · Quickshell over Astal | Plugin architecture over polish; animation ceiling over easy onboarding |
| `2026-07` | C# scoped to coursework only | Deliberately outside the real track — passing is the entire goal |

</details>

---

<p align="center">
<a href="https://github.com/volkansync"><img height="150em" src="https://github-readme-stats.vercel.app/api?username=volkansync&show_icons=true&bg_color=0E1628&border_color=1C2B4A&title_color=E6CC55&icon_color=E6CC55&text_color=EDE8DA&hide_border=false&count_private=true&include_all_commits=true" /></a>
<a href="https://github.com/volkansync"><img height="150em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=volkansync&layout=compact&bg_color=0E1628&border_color=1C2B4A&title_color=E6CC55&text_color=EDE8DA&hide_border=false" /></a>
</p>

<p align="center"><sub><i>"When you have eliminated the impossible, whatever remains, however improbable, must be the truth."</i><br/>— and then you measure it.</sub></p>
