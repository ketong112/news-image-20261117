# news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/ketong112/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/ketong112/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One image that sums up Tuesday 17 November 2026's world news: a dense
front page — 40 verified stories from six continents, three leads, six
regional sections and the day in figures, drawn deterministically with PIL.

## The three leads

1. **U.S. strikes Iran** — US jets hit missile sites on Qeshm Island
   after tanker attacks in the Strait of Hormuz.
2. **Kerch Bridge hit** — Ukrainian drones and missiles strike the
   Crimea bridge; a road span falls into the sea.
3. **NVIDIA in turmoil** — Board won't reinstate ex-CEO Jensen Huang
   after a spy scandal; revenue hits a record $115.8B.

Plus 37 more across Middle East & Africa, Europe, Asia-Pacific,
Americas, Tech & Markets, and Sport & Culture — including the U.S.
losing its measles-free status, the Ebola outbreak passing 11,000
cases in DR Congo, Japan scrambling jets, and Robert Pattinson named
the next James Bond.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` to
`/output/entry.png`. `entry.png` itself is drawn by `draw_image.py`
(Python + PIL, fixed text and layout, no network, no timestamps, no
randomness) — run it twice and the bytes are identical. The image is
1024 by 1024 pixels, 178,208 bytes.

---

<sub>Entered on [make.fun](https://make.fun/?ref=dmgw15y1&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
