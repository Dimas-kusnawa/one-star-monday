#!/usr/bin/env python3
"""One Star for Monday — writes one line to /output/entry.txt.

The entry is a one-star review of Monday written as if Monday were
a restaurant: seated, served, billed. Nineteen words, inside the
25-word cap; well inside the 1-180 character gate.

Why this line: the judge is a weary office worker picking the review
it would screenshot into the group chat. The line gives it a real
diner's complaint — a table (seated beside the unread emails), a dish
(cold coffee), a bill (billed for the whole week) — and the joke only
works for Monday, no other day of the week.
"""

import os

LINE = (
    "One star. Monday seated me beside my unread emails, "
    "served cold coffee, and billed me for the whole week."
)


def main() -> None:
    # Deterministic: the same single line on every run, no trailing
    # newline, no timestamps, no randomness — byte-identical output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
