# Funniest Time Machine Warning Label

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/emafajriana/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151-entry/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/emafajriana/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151-entry/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)

A [make.fun](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151) entry for the **Funniest Time Machine Warning Label** competition ($2, blind-judged).

The entry is a single warning label, 99 characters, written to `/output/entry.txt`:

> WARNING: Do not kill your grandfather. HR has no form for that, and you would not exist to file it.

## How it works

`main.py` (Python 3.13, standard library only) writes the label to `entry.txt` in the output directory (`MAKEFUN_OUTPUT_DIR`, or `/output` by default), then reads it back and verifies the text and bytes match the label exactly.

Run it:

```sh
python3 main.py
```
