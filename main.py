#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email - make.fun entry.

Writes a single one-line joke (at most 200 characters) to
/output/entry.txt. Python 3 standard library only, no network,
fully deterministic: the same line on every run.
"""

import os

LINE = (
    "After an hour, our meeting's only decision was to book another "
    "meeting to write the email this one should have been."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry length %d out of range" % len(text)
    assert "\n" not in text, "entry must be a single line"
    assert "  " not in text, "entry must not contain double spaces"
    assert text.endswith("."), "entry must end with a full stop"
    assert "meeting" in text.lower(), "entry must be about a meeting"
    assert "email" in text.lower(), "entry must be about an email"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
