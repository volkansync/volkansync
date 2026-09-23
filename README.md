<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/hero.gif?v=3" width="100%"/>

<div align="center">

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=800&size=22&pause=900&color=E6CC55&center=true&vCenter=true&width=720&lines=You+see%2C+but+you+do+not+observe.;Eliminate+the+impossible.;Measure+what+remains.;No+talent.+Preparation.;%E2%86%92+the+instrument+must+not+lie." alt="" />
</a>

<img src="https://img.shields.io/badge/-0E1628?style=flat-square" height="1" width="100%"/>

<a href="https://github.com/volkansync/field-notes"><img src="https://img.shields.io/badge/◆_field--notes-E6CC55?style=for-the-badge&labelColor=0E1628&color=0E1628" /></a>
<a href="https://www.linkedin.com/in/volkan-%C3%A7evik-90b1a937a"><img src="https://img.shields.io/badge/in-0E1628?style=for-the-badge&logo=linkedin&logoColor=E6CC55" /></a>
<a href="https://www.youtube.com/@volkansync"><img src="https://img.shields.io/badge/▶-0E1628?style=for-the-badge&logo=youtube&logoColor=E6CC55" /></a>
<img src="https://komarev.com/ghpvc/?username=volkansync&style=for-the-badge&color=E6CC55&labelColor=0E1628&label=OBSERVED" />

</div>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/divider.svg?v=2" width="100%"/>

<table>
<tr>
<td width="56%" valign="top">

```
◆  volkansync
   systems · infrastructure · security

▸  BASE    Eskişehir, TR
▸  OS      Arch / Wayland
▸  SHELL   zsh + neovim
▸  METHOD  eliminate → measure → fix

   "it works now" is not an explanation.
```

</td>
<td width="44%" valign="top">

| ◆ | TRACK | STATE |
|---|---|---|
| `01` | **field-notes** | 🟡 001 of 04 |
| `02` | **homelab** | 🟢 running |
| `03` | mobile product | 🟠 pre-release |
| `04` | **deutsch → B1** | 🟢 daily |
| `05` | RHCSA / LFCS | ⚪ queued |

</td>
</tr>
</table>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/divider.svg?v=2" width="100%"/>

<div align="center"><h3><code>◆ CASEFILES</code></h3><sub>most of the work is ruling things out</sub></div>

<br/>

<table>
<tr>
<td width="52%" valign="top">

> ### 🔴 `CASE 001`
> **Bluetooth audio dropping out**
> <sub>one channel first, alternating · two different headsets</sub>
>
> ~~faulty headphones~~ ~~wrong codec~~ ~~"just use 5 GHz"~~
>
> **→ 2.4 GHz band contention**
> <sub>power saving amplifies it · the link must be renegotiated</sub>
>
> # `152.5 → 18.3`
> <sub>failures/day · same network · **10 days at zero**</sub>

</td>
<td width="48%" valign="top">

**`CASE 002` · TLS certificate errors**
~~clock~~ ~~CA bundle~~ ~~the certificate~~
**→ ISP-level DNS blocking**
<sub>the resolution path, never the crypto</sub>

<br/>

**`CASE 003` · Anti-cheat 60099**
~~reinstall~~ ~~prefix reset~~
**→ `tr_TR` locale + missing font**
<sub>documented — survives the next reset</sub>

<br/>

**`CASE 004` · Shell dies every upgrade**
~~reinstall the package~~
**→ Qt ABI break**
<sub>found the trigger, not the symptom</sub>

<br/>

<sub>◆ full writeups + data + code →<br/>**[field-notes](https://github.com/volkansync/field-notes)**</sub>

</td>
</tr>
</table>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/divider.svg?v=2" width="100%"/>

<table>
<tr>
<td width="38%" valign="top">

<div align="center">

<h3><code>◆ INSTRUMENTS</code></h3>

<img src="https://skillicons.dev/icons?i=linux,bash,docker,nginx,postgres,git,python,rust&theme=dark&perline=4" />

</div>

`bt-dropout-test.sh`
<sub>2×2 harness · restores state on `Ctrl+C`</sub>

`analiz.py` ⚠️
<sub>**kept because it was wrong** — circular denominator</sub>

`analiz3.py` ✓
<sub>the one that held</sub>

</td>
<td width="62%" valign="top">

```mermaid
graph LR
    L((Linux)):::c --> N[networks]:::a
    L --> C[containers]:::a
    N --> S[security automation]:::b
    C --> K[cloud administration]:::b
    S -.-> X[RHCSA → CCNA → AZ-104]:::d
    K -.-> X
    classDef c fill:#E6CC55,stroke:#0A1120,color:#0A1120
    classDef a fill:#1C2B4A,stroke:#E6CC55,color:#EDE8DA
    classDef b fill:#2C4570,stroke:#E6CC55,color:#EDE8DA
    classDef d fill:#0E1628,stroke:#C4A93F,color:#C4A93F,stroke-dasharray:4 3
```

</td>
</tr>
</table>

<img src="https://raw.githubusercontent.com/volkansync/volkansync/main/assets/divider.svg?v=2" width="100%"/>

<div align="center">

<a href="https://github.com/volkansync"><img height="150em" src="https://github-readme-stats.vercel.app/api?username=volkansync&show_icons=true&bg_color=0E1628&border_color=1C2B4A&title_color=E6CC55&icon_color=E6CC55&text_color=EDE8DA&hide_border=false&count_private=true&include_all_commits=true" /></a>
<a href="https://github.com/volkansync"><img height="150em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=volkansync&layout=compact&bg_color=0E1628&border_color=1C2B4A&title_color=E6CC55&text_color=EDE8DA&hide_border=false" /></a>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/volkansync/volkansync/output/github-contribution-grid-snake-dark.svg" />
  <img alt="" src="https://raw.githubusercontent.com/volkansync/volkansync/output/github-contribution-grid-snake.svg" />
</picture>

<a href="https://github.com/volkansync"><img src="https://github-readme-activity-graph.vercel.app/graph?username=volkansync&bg_color=0E1628&color=EDE8DA&line=E6CC55&point=EDE8DA&area=true&area_color=1C2B4A&hide_border=false&border_color=1C2B4A&title_color=E6CC55" width="99%" /></a>

<br/>

<details>
<summary><sub><code>◆ CASE LOG</code> — expensive decisions, kept even when they read badly later</sub></summary>
<br/>

| | decision | why |
|---|---|---|
| `2026-09` | Closed the web agency; one product only | No revenue, fixed costs compounding |
| `2026-09` | Nothing new ships until the current one does | 18 categories scanned — a maintained free competitor in **every one** |
| `2026-09` | Deterministic by default; AI optional | When the credit runs out, it still has to work |
| `2026-09` | One repo, one deploy, one DB per product | A failure in one can't take down another |
| `2026-07` | Wayfire over Hyprland · Quickshell over Astal | Plugin architecture over polish |
| `2026-07` | C# scoped to coursework | Deliberately outside the real track |

</details>

<br/>

```
◆  "When you have eliminated the impossible, whatever remains,
    however improbable, must be the truth."

                                    → and then you measure it.
```

</div>
