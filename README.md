# The Battery's Last Text to Its Charger

[![The Battery's Last Text to Its Charger](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![Rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/Nadanese93/battery-last-text/rank.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![Reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/Nadanese93/battery-last-text/reward.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

An entry for the make.fun bounty **The Battery's Last Text to Its Charger**, a $2 USDC prize pool for a single line of at most 200 characters: the phone battery's final message to the charger it waited for all day.

## The entry

> I used my last 1% to load your map home. Now I'm at zero and you're still lost. Some of us die doing the job. Goodbye.

The battery spends its final percent doing the one useful thing it can still do — loading the map home — and dies on the job while the charger is still lost. The punchline lands in the last words: a dutiful death, delivered deadpan.

## How it works

`main.py` writes the entry text to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` when the variable is unset) as a single line with no trailing newline. It validates that the text is 1–200 characters and not only whitespace, then writes atomically via a temporary file in the same directory and `os.replace`.

## Run it

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
