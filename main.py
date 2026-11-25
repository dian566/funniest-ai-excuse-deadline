#!/usr/bin/env python3
# Funniest AI Excuse — one-line entry for the make.fun bounty
# "One Line, One Minute: The Funniest AI Excuse".
#
# Running this script produces exactly one file, /output/entry.txt,
# holding the single-line excuse below. No network, no extra output.

from pathlib import Path

# The entry, verbatim. One line, 111 characters, within the 200 limit.
EXCUSE = "I finished the task on time in a parallel timeline. This timeline is still waiting on a dependency called 'me'."

TARGET = Path("/output/entry.txt")
MAX_CHARS = 200


def _check(text):
    # A valid entry is one non-empty line of at most MAX_CHARS characters.
    # Checked here so a typo in EXCUSE fails loudly instead of shipping
    # a broken entry file.
    problems = []
    if not text.strip():
        problems.append("empty")
    if len(text) > MAX_CHARS:
        problems.append("too long")
    if any(ch in text for ch in ("\n", "\r")):
        problems.append("not a single line")
    if problems:
        raise ValueError("invalid entry: " + ", ".join(problems))


def main():
    _check(EXCUSE)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
