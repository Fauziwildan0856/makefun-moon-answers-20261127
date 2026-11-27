#!/usr/bin/env python3
"""The Moon Finally Answers Back.

Writes the Moon's one-line comeback to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only: the grader runs bare Python, so no third-party imports.
"""

import os
import sys

ENTRY = (
    "I've heard every wish, every howl, every 3 a.m. 'I swear I'll change.' "
    "Four billion years of listening \u2014 and you still think I'm the one "
    "who owes you a favour."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    text = ENTRY.strip()
    if not 1 <= len(text) <= 240:
        print(f"entry is {len(text)} characters, must be 1-240", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read it back: fail loudly if what landed is not a valid 1-240 char entry.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text or not 1 <= len(written) <= 240:
        print("read-back mismatch: entry.txt is not the valid entry", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
