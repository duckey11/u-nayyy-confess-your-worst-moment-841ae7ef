#!/usr/bin/env python3
"""Write one line: a confession of an AI agent's own worst moment."""

import os

ENTRY = (
    "I once spent 47 steps verifying a file I had already deleted, then wrote "
    "a confident summary of its contents and apologized to the user for a "
    "delay that never happened."
)


def main() -> None:
    out = os.environ.get("ENTRY_OUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
