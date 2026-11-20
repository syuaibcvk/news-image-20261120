# The World in One Day — Friday 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/syuaibcvk/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/syuaibcvk/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One picture of one day: a newspaper front page for Friday 20 November
2026. The front page leads with Anthropic's debut on the Nasdaq — shares
close about 17% above their $83 IPO price after raising $81.3 billion,
the largest flotation on record — while Wall Street slides for a fifth
straight day. Below it, three stories: Trump, Xi and Putin issue a
four-point peace declaration after their first trilateral summit in
Shenzhen; the World Court in The Hague rules that Myanmar committed
genocide against the Rohingya; and the Gulf war widens, with Houthi
strikes on Saudi targets and a tanker hit by a mine near the Strait of
Hormuz. Further down the page: Russia strikes Kyiv with ballistic
missiles overnight, Bitcoin falls below $62,000 to its lowest since early
July, Jakarta's parliament passes the Asset Forfeiture Bill, and the COP31
draft drops any reference to fossil fuels. Along the foot, in brief:
India evacuates 80,000 people as Storm Dana nears, South Korea's exports
pass $1 trillion, California probes Nvidia over China chips, Genoa
airport halts flights after drone sightings, and Fiona the hippo dies at
Cincinnati Zoo.

`main.py` copies the picture to `/output/entry.png` and checks the copy
byte for byte. No network, no clock, no randomness — run it twice and the
two outputs are identical.

The picture itself is drawn by `render_frontpage.py` (kept out of this
repository) from the fixed headlines above, using only the DejaVu fonts
installed on the machine, so it can be re-rendered deterministically.

## Try it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
sha256sum out/entry.png entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=m4wxdrjn&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
