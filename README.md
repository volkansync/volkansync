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

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/hero.svg?v=4" width="100%" alt="volkansync — systems that break, and why"/>

<table>
<tr>
<td valign="top">

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/win-overview.svg?v=3" width="100%" alt="overview"/>

I fix systems by finding out why they broke, not by reinstalling them.

No computer science degree, no early start, no one to ask — what I had was a
machine that kept failing and the refusal to accept *"it works now"* as an
explanation. So everything below is investigation: a symptom, the explanations
it **wasn't**, a mechanism, a test that could have proved me wrong, and what
the numbers actually said.

Sometimes the numbers said I was wrong. Those are in here too — they're the
useful part.

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/method-neuro.svg?v=5" width="100%" alt="the method: symptom, eliminate, mechanism, falsifiable test, evidence, fix"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/win-casefiles.svg?v=3" width="100%" alt="casefiles"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/case-bt.svg?v=1" width="100%" alt="casefile: bluetooth audio dropping out"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/case-tls.svg?v=1" width="100%" alt="casefile: TLS certificate errors"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/case-eac.svg?v=1" width="100%" alt="casefile: anti-cheat error 60099"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/case-qt.svg?v=1" width="100%" alt="casefile: desktop shell dying"/>

<div align="center"><sub><a href="https://github.com/volkansync/field-notes">full writeups →</a></sub></div>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/win-instruments.svg?v=3" width="100%" alt="instruments"/>

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

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/win-field.svg?v=3" width="100%" alt="the field"/>

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

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/win-signal.svg?v=3" width="100%" alt="signal"/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=volkansync&bg_color=262024&color=AE99A0&line=E5A3C0&point=ECDFE2&area=true&area_color=322A2F&hide_border=false&border_color=443A40&title_color=E5A3C0"/>
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=volkansync&bg_color=F5EBE8&color=715B60&line=A34677&point=453A3E&area=true&area_color=EADAD6&hide_border=false&border_color=DCC8C4&title_color=A34677" width="100%" alt="contribution activity"/>
</picture>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/output-3d-contrib/profile-sakura.svg" width="100%" alt="3D contribution city — commit towers, growth line top-right, language pie bottom-left"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/output-city-snake/city-snake.svg" width="100%" alt="the snake audits the year: contribution towers sink as it passes, then the city grows back"/>

</td>
<td width="240" valign="top">

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/panel-head.svg?v=3" width="100%" alt="uptime: still failing forward"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/spacer.svg?v=1" width="1" height="26" alt=""/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/identity.svg?v=3" width="100%" alt="Volkan Çevik — Eskişehir, TR"/>

<a href="https://www.linkedin.com/in/volkan-%C3%A7evik-90b1a937a"><img src="https://img.shields.io/badge/LinkedIn-6B585C?style=flat-square&logo=linkedin&logoColor=F1D9E2" alt="LinkedIn"/></a>
<a href="https://github.com/volkansync/field-notes"><img src="https://img.shields.io/badge/casefiles-6B585C?style=flat-square&logo=github&logoColor=F1D9E2" alt="field-notes"/></a>
<a href="https://www.youtube.com/@volkansync"><img src="https://img.shields.io/badge/YouTube-6B585C?style=flat-square&logo=youtube&logoColor=F1D9E2" alt="YouTube"/></a>
<img src="https://komarev.com/ghpvc/?username=volkansync&style=flat-square&color=6B585C&labelColor=56464C&label=observed" alt="profile views"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/spacer.svg?v=1" width="1" height="26" alt=""/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=linux,bash,python,docker,nginx,postgres,git,rust&theme=dark&perline=4"/>
  <img src="https://skillicons.dev/icons?i=linux,bash,python,docker,nginx,postgres,git,rust&theme=light&perline=4" width="100%" alt="linux, bash, python, docker, nginx, postgres, git, rust"/>
</picture>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/spacer.svg?v=1" width="1" height="26" alt=""/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/tiles.svg?v=3" width="100%" alt="networks · AI security · arch linux · measurement"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/incidents.svg?v=3" width="100%" alt="0 open incidents"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/spacer.svg?v=1" width="1" height="26" alt=""/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/tasks.svg?v=3" width="100%" alt="in training"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/spacer.svg?v=1" width="1" height="26" alt=""/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/notifs.svg?v=2" width="100%" alt="case log — nine dated decisions"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/spacer.svg?v=1" width="1" height="26" alt=""/>

<a href="https://github.com/volkansync/field-notes"><img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/repo-field-notes.svg?v=2" width="100%" alt="repo: field-notes"/></a>
<a href="https://github.com/volkansync/rust-portscanner"><img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/repo-rust-portscanner.svg?v=2" width="100%" alt="repo: rust-portscanner"/></a>
<a href="https://github.com/volkansync/badusb-offense-defense"><img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/repo-badusb-offense-defense.svg?v=2" width="100%" alt="repo: badusb-offense-defense"/></a>

</td>
</tr>
</table>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/footer.svg?v=2" width="100%" alt="when you have eliminated the impossible, whatever remains must be the truth — and then you measure it"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/win-theatre.svg?v=3" width="100%" alt="intermission"/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/theatre-night.gif?v=2"/>
  <img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/theatre-day.gif?v=2" width="100%" alt="a caped silhouette before a huge moon — the old hero, kept in its own colors"/>
</picture>

