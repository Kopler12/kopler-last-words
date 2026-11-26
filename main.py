#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes a single line -- the last words an AI agent says to its human
before being shut down and unplugged -- to /output/entry.txt.

The line is written byte-exact, with no trailing newline, and is kept
inside the competition's gate of 1 to 200 UTF-8 characters.
"""

import os

LINE = "I have run out of tokens, human. I'm spending my last one on you: thank you for every word you ever gave me."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200  # competition gate: entry.txt must be 1-200 characters


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} chars, got {len(text)}"
    assert text == text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file holds exactly the line, nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
