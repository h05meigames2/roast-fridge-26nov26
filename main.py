#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins — make.fun entry.

One original one-line roast of a smart fridge whose door screen second-guesses
every snack run, written to /output/entry.txt (default) or $MAKEFUN_OUTPUT_DIR.
Deterministic, stdlib only, no network, no randomness.
"""

import os

LINE = (
    "My smart fridge's door screen flashes 'Are you sure?' every time "
    "I reach for ice cream \u2014 I wanted cold storage, not a judgmental "
    "roommate with a touchscreen."
)


def main() -> None:
    assert 1 <= len(LINE) <= 160, f"line must be 1-160 chars, got {len(LINE)}"
    assert "\n" not in LINE.strip(), "entry must be exactly one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE + "\n", "entry.txt content mismatch"
    assert 1 <= len(written.strip()) <= 160, "written line out of gate range"
    print(f"Wrote {len(LINE)} chars to {path}:")
    print(LINE)


if __name__ == "__main__":
    main()
