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

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/hero.svg?v=2" width="100%" alt="volkansync — systems that break, and why"/>

<table>
<tr>
<td width="26" valign="top">

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/bar.svg?v=2" width="26" alt=""/>

</td>
<td valign="top">

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/win-overview.svg?v=2" width="100%" alt="overview"/>

I fix systems by finding out why they broke, not by reinstalling them.

No computer science degree, no early start, no one to ask — what I had was a
machine that kept failing and the refusal to accept *"it works now"* as an
explanation. So everything below is investigation: a symptom, the explanations
it **wasn't**, a mechanism, a test that could have proved me wrong, and what
the numbers actually said.

Sometimes the numbers said I was wrong. Those are in here too — they're the
useful part.

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/method-neuro.svg?v=5" width="100%" alt="the method: symptom, eliminate, mechanism, falsifiable test, evidence, fix"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/win-casefiles.svg?v=2" width="100%" alt="casefiles"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/case-bt.svg?v=1" width="100%" alt="casefile: bluetooth audio dropping out"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/case-tls.svg?v=1" width="100%" alt="casefile: TLS certificate errors"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/case-eac.svg?v=1" width="100%" alt="casefile: anti-cheat error 60099"/>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/case-qt.svg?v=1" width="100%" alt="casefile: desktop shell dying"/>

<div align="center"><sub><a href="https://github.com/volkansync/field-notes">full writeups →</a></sub></div>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/win-instruments.svg?v=2" width="100%" alt="instruments"/>

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

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/win-field.svg?v=2" width="100%" alt="the field"/>

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

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/win-theatre.svg?v=1" width="100%" alt="intermission"/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/theatre-night.gif?v=1"/>
  <img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/theatre-day.gif?v=1" width="100%" alt="a caped silhouette before a huge sakura moon — the old hero, recolored for this desktop"/>
</picture>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/win-signal.svg?v=2" width="100%" alt="signal"/>

<div align="center">

</td>
</tr>
</table>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/footer.svg?v=2" width="100%" alt="when you have eliminated the impossible, whatever remains must be the truth — and then you measure it"/>
