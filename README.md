<div align="center">

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/hero.gif?v=3" width="100%"/>

<h1>volkansync</h1>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=19&pause=1000&color=E6CC55&center=true&vCenter=true&width=680&lines=You+see%2C+but+you+do+not+observe.;Eliminate+the+impossible.+Measure+what+remains.;No+talent.+Preparation%2C+and+the+right+instrument.;Linux+%E2%86%92+networks+%E2%86%92+cloud+%E2%86%92+security." alt="" />
</a>

<br/>

<img src="https://img.shields.io/badge/systems%20%26%20infrastructure-0E1628?style=for-the-badge&labelColor=E6CC55&color=0E1628" />
<img src="https://img.shields.io/badge/Eskişehir,%20TR-0E1628?style=for-the-badge&labelColor=1C2B4A&color=0E1628" />

<br/><br/>

<a href="https://www.linkedin.com/in/volkan-%C3%A7evik-90b1a937a">
  <img src="https://img.shields.io/badge/LinkedIn-1C2B4A?style=flat-square&logo=linkedin&logoColor=E6CC55" />
</a>
<a href="https://github.com/volkansync/field-notes">
  <img src="https://img.shields.io/badge/casefiles-1C2B4A?style=flat-square&logo=github&logoColor=E6CC55" />
</a>
<a href="https://www.youtube.com/@volkansync">
  <img src="https://img.shields.io/badge/YouTube-1C2B4A?style=flat-square&logo=youtube&logoColor=E6CC55" />
</a>
<img src="https://komarev.com/ghpvc/?username=volkansync&style=flat-square&color=1C2B4A&labelColor=0E1628&label=observed" />

</div>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/divider.svg?v=2" width="100%"/>

I fix systems by finding out why they broke, not by reinstalling them.

No computer science degree, no early start, no one to ask — what I had was a machine
that kept failing and the refusal to accept *"it works now"* as an explanation. So the
work below is mostly investigation: a symptom, the explanations it **wasn't**, a
mechanism, a test that could have proved me wrong, and what the numbers actually said.

Sometimes the numbers said I was wrong. Those are in here too — they're the useful part.

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/method.svg?v=2" width="100%"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/divider.svg?v=2" width="100%"/>

<div align="center">

## `[ CASEFILES ]`

<sub>real failures on real machines — <a href="https://github.com/volkansync/field-notes">full writeups</a></sub>

</div>

<table>
<tr>
<td width="30%" valign="top"><b>SYMPTOM</b></td>
<td width="33%" valign="top"><b>THE MISDIRECTION</b></td>
<td width="37%" valign="top"><b>WHAT IT ACTUALLY WAS</b></td>
</tr>

<tr>
<td valign="top"><b>Bluetooth audio dropping out</b><br/><sub>one channel first, alternating, then both — on two different headsets</sub></td>
<td valign="top">"Your headphones are faulty." "Change the codec." "Just move to 5&nbsp;GHz."<br/><sub>all three tested, all three wrong</sub></td>
<td valign="top"><b>2.4&nbsp;GHz band contention</b>, amplified by Wi-Fi power saving.<br/><br/><code>152.5 → 18.3 failures/day</code> on the same network · <b>10 days at zero</b><br/><sub>and a second step no guide mentions: the Bluetooth link has to be renegotiated, or the fix appears not to work</sub></td>
</tr>

<tr>
<td valign="top"><b>TLS certificate errors</b><br/><sub>on one specific service, certificate chain intact</sub></td>
<td valign="top">"Your clock is wrong." "Reinstall the CA bundle."</td>
<td valign="top"><b>ISP-level DNS blocking.</b> The certificate was never involved — the resolution path was. Fixed per-connection, not system-wide.</td>
</tr>

<tr>
<td valign="top"><b>Anti-cheat error 60099</b><br/><sub>on an otherwise healthy install</sub></td>
<td valign="top">"Reinstall the game." "Reset the prefix."<br/><sub>works once, breaks again</sub></td>
<td valign="top"><b><code>tr_TR</code> locale + a missing Windows font.</b> An opaque vendor error code traced to a locale dependency — documented so it survives the next prefix reset.</td>
</tr>

<tr>
<td valign="top"><b>Desktop shell dying</b><br/><sub>after every system upgrade, reliably</sub></td>
<td valign="top">"Reinstall the package."<br/><sub>monthly, forever</sub></td>
<td valign="top"><b>Qt ABI break.</b> The shell was compiled against the previous <code>qt6-base</code>. Found the recurring trigger instead of re-fixing the symptom each month.</td>
</tr>
</table>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/divider.svg?v=2" width="100%"/>

<div align="center">

## `[ INSTRUMENTS ]`

<sub>the hard part is rarely the fault — it's building a measurement that doesn't lie</sub>

</div>

<table>
<tr>
<td width="34%" valign="top">

**`bt-dropout-test.sh`**

A 2×2 harness. Pins the Wi-Fi band by BSSID, toggles power saving, samples PipeWire
xruns and signal strength per arm, and restores every setting on exit — including on
`Ctrl+C`, so a half-finished run can't leave the network pinned.

</td>
<td width="33%" valign="top">

**`analiz.py`** — *kept because it was wrong*

Normalised failures per "Bluetooth-active hour." The denominator was driven by the
same failures as the numerator, so it hid the very effect it was measuring. Left in
the repo on purpose.

</td>
<td width="33%" valign="top">

**`analiz3.py`** — *the one that held*

Per-day, per-network, with usage detected from events that fire **independently of
errors**. Only then could "no failures" be told apart from "not used."

</td>
</tr>
</table>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/divider.svg?v=2" width="100%"/>

<div align="center">

## `[ THE FIELD ]`

<img src="https://skillicons.dev/icons?i=linux,bash,docker,nginx,postgres,git,python,rust&theme=dark&perline=8" />

</div>

<table>
<tr><td width="33%" valign="top">

**Linux & systems**

Arch on Wayland, daily driver. At home in the parts that break: `systemd` units,
NetworkManager, the audio and display stacks, ABI breakage after upgrades.

</td><td width="33%" valign="top">

**Networks & services**

Reverse proxies, TLS, DNS resolution paths, containerised services each with their
own database, deployment via Coolify. Wrote a threaded TCP port scanner in Rust to
learn the layer from packets rather than from a diagram.

</td><td width="33%" valign="top">

**Direction**

Cloud administration and security automation. The certifications below are the
near-term proof — and none of them are finished yet.

</td></tr>
</table>

<div align="center">

### `[ IN TRAINING ]`

<sub>carried until earned — <code>queued</code> means queued, not modest</sub>

| | |
|---|---|
| **German → B1** | in progress · daily, no exceptions |
| **RHCSA** / **LFCS** | queued — first up |
| **CCNA** | queued |
| **AZ-104** / **AWS SAA** | queued |

</div>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/divider.svg?v=2" width="100%"/>

<div align="center">

## `[ CASE LOG ]`

<sub>decisions that were expensive to make, kept even when they read badly later</sub>

</div>

| | decision | why |
|---|---|---|
| `2026-09` | Closed the web agency; everything moved to one product | No revenue, and the fixed costs compounded monthly |
| `2026-09` | Nothing new starts until the current product ships | A scan across 18 categories found a maintained free competitor in **every one** — shallow tools don't differentiate |
| `2026-09` | Deterministic logic is the default; AI is an optional layer | When the API credit runs out, the product still has to work |
| `2026-09` | One repo, one deployment, one database per product | A failure in one must not be able to take down another |
| `2026-07` | Wayfire over Hyprland · Quickshell over Astal | Plugin architecture over polish; animation ceiling over easy onboarding |
| `2026-07` | C# scoped to coursework only | Deliberately outside the real track — passing is the entire goal |

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/divider.svg?v=2" width="100%"/>

<div align="center">

## `[ SIGNAL ]`

<a href="https://github.com/volkansync">
  <img height="170em" src="https://github-readme-stats.vercel.app/api?username=volkansync&show_icons=true&bg_color=0E1628&border_color=1C2B4A&title_color=E6CC55&icon_color=E6CC55&text_color=EDE8DA&hide_border=false&count_private=true&include_all_commits=true" />
</a>
<a href="https://github.com/volkansync">
  <img height="170em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=volkansync&layout=compact&bg_color=0E1628&border_color=1C2B4A&title_color=E6CC55&text_color=EDE8DA&hide_border=false" />
</a>

<br/><br/>

<a href="https://github.com/volkansync">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=volkansync&bg_color=0E1628&color=EDE8DA&line=E6CC55&point=EDE8DA&area=true&area_color=1C2B4A&hide_border=false&border_color=1C2B4A&title_color=E6CC55" width="98%" />
</a>

<br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/volkansync/volkansync/output/github-contribution-grid-snake-dark.svg" />
  <img alt="" src="https://raw.githubusercontent.com/volkansync/volkansync/output/github-contribution-grid-snake.svg" />
</picture>

</div>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/divider.svg?v=2" width="100%"/>

<div align="center">

```
"When you have eliminated the impossible, whatever remains,
 however improbable, must be the truth."

                                    — and then you measure it.
```

<sub>this page changes when something underneath it does — not on a schedule</sub>

</div>
