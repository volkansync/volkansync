<!--
THESIS: the profile IS the owner's desktop — a quickshell rice rendered in
GitHub markdown (thin bar | workspace windows | side panel); refuses the
stacked-banner profile template.
OWN-WORLD: Material-You "sakura shell": blush surfaces #F5EBE8/#EADAD6 (day),
plum-charcoal #262024/#322A2F (night), plum ink, sakura-rose + teal + coral
accents, 20-30px radii, tonal elevation, pill chips; system sans, mono only
for measurements. System stack is a GitHub-sandbox concession.
STORY: visitor recognizes a living Linux desktop; windows hold the
investigations, the panel holds who runs the machine; leaves believing
"systems detective, aimed at AI security" and opens field-notes.
FIRST VIEWPORT: full-width Fuji/sakura wallpaper with cycling quotes; below,
the shell opens — bar with workspace pills, overview window (intro + neural
method), panel top (uptime + identity).
FORM: user-pinned rice (end-4 "ii"); pinned direction beats the roll.
FINISH: unreviewed and undocumented is unfinished; this build ends with the
finish review, the verdict, DESIGN.md, and every shipping raster carrying its
provenance.
-->

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/hero.svg?v=1" width="100%" alt="volkansync — systems that break, and why"/>

<table>
<tr>
<td width="26" valign="top">

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/bar.svg?v=1" width="26" alt=""/>

</td>
<td valign="top">

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/win-overview.svg?v=1" width="100%" alt="overview"/>

I fix systems by finding out why they broke, not by reinstalling them.

No computer science degree, no early start, no one to ask — what I had was a
machine that kept failing and the refusal to accept *"it works now"* as an
explanation. So everything below is investigation: a symptom, the explanations
it **wasn't**, a mechanism, a test that could have proved me wrong, and what
the numbers actually said.

Sometimes the numbers said I was wrong. Those are in here too — they're the
useful part.

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/method-neuro.svg?v=4" width="100%" alt="the method: symptom, eliminate, mechanism, falsifiable test, evidence, fix"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/win-casefiles.svg?v=1" width="100%" alt="casefiles"/>

**Bluetooth audio dropping out** <sub>one channel first, alternating, then both — on two different headsets</sub><br/>
~~"your headphones are faulty"~~ · ~~"change the codec"~~ · ~~"just move to 5 GHz"~~<br/>
**2.4 GHz band contention**, amplified by Wi-Fi power saving — `152.5 → 18.3 failures/day` on the same network, **10 days at zero**<br/>
<sub>and a second step no guide mentions: renegotiate the Bluetooth link, or the fix appears not to work</sub>

**TLS certificate errors** <sub>on one specific service, certificate chain intact</sub><br/>
~~"your clock is wrong"~~ · ~~"reinstall the CA bundle"~~<br/>
**ISP-level DNS blocking.** The certificate was never involved — the resolution path was. Fixed per-connection, not system-wide.

**Anti-cheat error 60099** <sub>on an otherwise healthy install</sub><br/>
~~"reinstall the game"~~ · ~~"reset the prefix"~~ <sub>(works once, breaks again)</sub><br/>
**`tr_TR` locale + a missing Windows font.** An opaque vendor error traced to a locale dependency — documented so it survives the next prefix reset.

**Desktop shell dying** <sub>after every system upgrade, reliably</sub><br/>
~~"reinstall the package"~~ <sub>(monthly, forever)</sub><br/>
**Qt ABI break.** The shell was compiled against the previous `qt6-base`. Found the recurring trigger instead of re-fixing the symptom each month.

<div align="center"><sub><a href="https://github.com/volkansync/field-notes">full writeups →</a></sub></div>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/win-instruments.svg?v=1" width="100%" alt="instruments"/>

**`bt-dropout-test.sh`** — a 2×2 harness. Pins the Wi-Fi band by BSSID, toggles
power saving, samples PipeWire xruns and signal strength per arm, and restores
every setting on exit — including on `Ctrl+C`, so a half-finished run can't
leave the network pinned.

**`analiz.py`** — *kept because it was wrong.* Normalised failures per
"Bluetooth-active hour"; the denominator was driven by the same failures as
the numerator, so it hid the very effect it was measuring. Left in the repo
on purpose.

**`analiz3.py`** — *the one that held.* Per-day, per-network, with usage
detected from events that fire **independently of errors**. Only then could
"no failures" be told apart from "not used."

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/win-field.svg?v=1" width="100%" alt="the field"/>

**Where I work now** — Arch on Wayland, daily driver. At home in the parts
that break: `systemd` units, NetworkManager, the audio and display stacks,
ABI breakage after upgrades. Reverse proxies, TLS, DNS resolution paths,
containerised services with their own databases.

**What it's turning into** — security. Wrote a threaded TCP port scanner in
Rust to learn the layer from packets rather than from a diagram — the same
instinct as the casefiles: find out what is actually happening, not what is
supposed to.

**Where it's going** — **AI security.** Everyone is shipping agents; very few
people can break them. Prompt injection, tool-call abuse, retrieval poisoning,
model leakage. <sub>Stated as a direction, not a claim — the evidence isn't
here yet. When it is, it will be in <code>field-notes</code> like everything
else.</sub>

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=linux,bash,python,docker,nginx,postgres,git,rust&theme=dark&perline=8"/>
  <img src="https://skillicons.dev/icons?i=linux,bash,python,docker,nginx,postgres,git,rust&theme=light&perline=8" alt="linux, bash, python, docker, nginx, postgres, git, rust"/>
</picture>

</div>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/win-signal.svg?v=1" width="100%" alt="signal"/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=volkansync&bg_color=262024&color=AE99A0&line=E5A3C0&point=ECDFE2&area=true&area_color=322A2F&hide_border=false&border_color=443A40&title_color=E5A3C0"/>
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=volkansync&bg_color=F5EBE8&color=715B60&line=A34677&point=453A3E&area=true&area_color=EADAD6&hide_border=false&border_color=DCC8C4&title_color=A34677" width="100%" alt="contribution activity"/>
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/volkansync/volkansync/output/github-contribution-grid-snake-dark.svg"/>
  <img src="https://raw.githubusercontent.com/volkansync/volkansync/output/github-contribution-grid-snake.svg" width="100%" alt=""/>
</picture>

</td>
<td width="240" valign="top">

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/panel-head.svg?v=1" width="100%" alt="uptime: still failing forward"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/identity.svg?v=2" width="100%" alt="Volkan Çevik — Eskişehir, TR"/>

<a href="https://www.linkedin.com/in/volkan-%C3%A7evik-90b1a937a"><img src="https://img.shields.io/badge/LinkedIn-6B585C?style=flat-square&logo=linkedin&logoColor=F1D9E2" alt="LinkedIn"/></a>
<a href="https://github.com/volkansync/field-notes"><img src="https://img.shields.io/badge/casefiles-6B585C?style=flat-square&logo=github&logoColor=F1D9E2" alt="field-notes"/></a>
<a href="https://www.youtube.com/@volkansync"><img src="https://img.shields.io/badge/YouTube-6B585C?style=flat-square&logo=youtube&logoColor=F1D9E2" alt="YouTube"/></a>
<img src="https://komarev.com/ghpvc/?username=volkansync&style=flat-square&color=6B585C&labelColor=56464C&label=observed" alt="profile views"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/tiles.svg?v=1" width="100%" alt="networks · AI security · arch linux · measurement"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/incidents.svg?v=1" width="100%" alt="0 open incidents"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/tasks.svg?v=1" width="100%" alt="in training"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/notifs.svg?v=1" width="100%" alt="case log — nine dated decisions"/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=volkansync&show_icons=true&bg_color=262024&border_color=443A40&title_color=E5A3C0&icon_color=7FCBD0&text_color=ECDFE2&border_radius=24&count_private=true&include_all_commits=true"/>
  <img src="https://github-readme-stats.vercel.app/api?username=volkansync&show_icons=true&bg_color=F5EBE8&border_color=DCC8C4&title_color=A34677&icon_color=2E7F84&text_color=453A3E&border_radius=24&count_private=true&include_all_commits=true" width="100%" alt="github stats"/>
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=volkansync&layout=compact&bg_color=262024&border_color=443A40&title_color=E5A3C0&text_color=ECDFE2&border_radius=24"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=volkansync&layout=compact&bg_color=F5EBE8&border_color=DCC8C4&title_color=A34677&text_color=453A3E&border_radius=24" width="100%" alt="top languages"/>
</picture>

</td>
</tr>
</table>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/footer.svg?v=1" width="100%" alt="when you have eliminated the impossible, whatever remains must be the truth — and then you measure it"/>
