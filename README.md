<div align="center">

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/hero.gif?v=3" width="100%"/>

<h1>volkansync</h1>

<a href="https://readme-typing-svg.demolab.com">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=19&pause=1000&color=E6CC55&center=true&vCenter=true&width=680&lines=You+see%2C+but+you+do+not+observe.;Eliminate+the+impossible.+Measure+what+remains.;No+talent.+Preparation%2C+and+the+right+instrument.;Linux+%E2%86%92+networks+%E2%86%92+security+%E2%86%92+AI+security." alt="" />
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
</table>

<div align="center">

### `[ INSTRUMENTS ]`

<sub>the tools behind the casefiles — the hard part is rarely the fault, it's building a measurement that doesn't lie</sub>

</div>

**`bt-dropout-test.sh`**

A 2×2 harness. Pins the Wi-Fi band by BSSID, toggles power saving, samples PipeWire
xruns and signal strength per arm, and restores every setting on exit — including on
`Ctrl+C`, so a half-finished run can't leave the network pinned.

**`analiz.py`** — *kept because it was wrong*

Normalised failures per "Bluetooth-active hour." The denominator was driven by the
same failures as the numerator, so it hid the very effect it was measuring. Left in
the repo on purpose.

**`analiz3.py`** — *the one that held*

Per-day, per-network, with usage detected from events that fire **independently of
errors**. Only then could "no failures" be told apart from "not used."

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/divider.svg?v=2" width="100%"/>

<div align="center">

## `[ THE FIELD ]`

<img src="https://skillicons.dev/icons?i=linux,bash,python,docker,nginx,postgres,git,rust&theme=dark&perline=8" />

</div>

**`▸ where I work now`**

Arch on Wayland, daily driver. At home in the parts that break: `systemd` units,
NetworkManager, the audio and display stacks, ABI breakage after upgrades. Reverse
proxies, TLS, DNS resolution paths, containerised services with their own databases.

**`▸ what it's turning into`**

Security. Wrote a threaded TCP port scanner in Rust to learn the layer from packets
rather than from a diagram — the same instinct as the casefiles above: find out what
is actually happening, not what is supposed to.

**`▸ where it's going — AI security`**

Everyone is shipping agents; very few people can break them. Prompt injection,
tool-call abuse, retrieval poisoning, model leakage.

<sub>Stated as a direction, not a claim — the evidence isn't here yet. When it is, it
will be in `field-notes` like everything else.</sub>

<div align="center">

### `[ IN TRAINING ]`

<sub>carried until earned — <code>queued</code> means queued, not modest</sub>

| | |
|---|---|
| **German → B1** | in progress · daily, no exceptions |
| **Python, properly** | in progress · now the primary language |
| **ML fundamentals** | in progress · embeddings, retrieval, evaluation — enough to break it, then enough to build it |
| **RHCSA** / **LFCS** | queued — first certification up |
| Rust | secondary · systems and tooling, not the main track |

</div>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/divider.svg?v=2" width="100%"/>

<div align="center">

## `[ CASE LOG ]`

<sub>decisions that were expensive to make, kept even when they read badly later</sub>

</div>

| | decision | why |
|---|---|---|
| `2026-09` | **Main track moved to AI security.** Cloud demoted from the goal to the substrate | The interesting gap is between security and ML, and it rewards demonstrated work over credentials |
| `2026-09` | **Python over Rust as the primary language** | ML lives in Python. Rust stays for systems and tooling — they are different tracks, not competitors |
| `2026-09` | Automated video pipeline paused after the TTS stage | Local Turkish TTS could not hold the `ı`/`i` distinction or carry tone. Shipping it would have meant shipping something I could hear was bad |
| `2026-09` | Closed the web agency; everything moved to one product | No revenue, and the fixed costs compounded monthly |
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
