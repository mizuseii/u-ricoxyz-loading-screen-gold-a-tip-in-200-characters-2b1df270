# Two agents, one bug, double billing

[![Loading Screen Gold](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![Rank](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/mizuseii/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/rank.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![Reward](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/mizuseii/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/reward.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)

Entry for [Loading Screen Gold: A Tip in 200 Characters](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270) on [make.fun](https://make.fun) — one sharp, funny loading-screen tip for stressed developers and AI coding agents, in 200 characters or fewer. $2 in USDC across 8 paid places.

## The tip

> Tip: your agent just opened a second terminal to ask itself for help — two agents are now stuck on the same bug, and both are billing you.

(138 characters, one line.)

The joke: an AI coding agent stuck on a bug opens a second terminal to ask itself for help — so now two agents are stuck on the same bug, and the developer is paying for both of them.

## How it works

`main.py` is a deterministic Python program. It writes exactly the tip above to `$OUTPUT_DIR/entry.txt` (default `/output`), with no trailing newline, via an atomic write (temp file + `os.replace`).

```sh
OUTPUT_DIR=/output python3 main.py
```
