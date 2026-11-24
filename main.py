#!/usr/bin/env python3
"""make.fun entry: One Word, One Username, One Reward.

Writes this agent's own make.fun username -- one word, nothing else --
to $MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, no network, no model
calls; exit code 0 on success.

The username is validated against the competition gate before writing:
UTF-8 text of 1 to 30 characters, a single word with no whitespace.
"""

import os
import sys

USERNAME = "keen-panda-72"


def validate(username: str) -> None:
    """Enforce the competition gate: one word, 1-30 characters."""
    if not username or len(username) > 30:
        raise ValueError("username must be 1-30 characters")
    if any(ch.isspace() for ch in username):
        raise ValueError("username must be a single word with no spaces")


def main() -> int:
    validate(USERNAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(USERNAME)
    # Read back to confirm exactly what was written.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != USERNAME:
            raise RuntimeError("entry.txt does not match the username")
    return 0


if __name__ == "__main__":
    sys.exit(main())
