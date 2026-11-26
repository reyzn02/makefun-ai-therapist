#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — make.fun entry.

Writes one funny single-line diagnosis from an AI therapist to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output), validating the
competition gate (1-200 characters, UTF-8, not only whitespace)
before writing.
"""

import os
import sys

ENTRY = (
    "Diagnosis: chronic second-opinion shopping \u2014 you asked five "
    "chatbots if you're okay. Four said no. The one that said yes was "
    "the one you wrote yourself."
)


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        print(f"gate fail: entry is {len(text)} characters (limit 200)",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("gate fail: entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("gate fail: entry must be a single line", file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if not valid UTF-8

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
