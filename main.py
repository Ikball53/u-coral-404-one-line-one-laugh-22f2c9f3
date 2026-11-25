"""One Line, One Laugh - entry v1.

Writes a single deadpan one-liner to entry.txt, byte-exact,
with no trailing newline and no internal line breaks.
"""

import hashlib
import os

# The joke: an expensive posture fix, ignored in the most literal way,
# with the fitness tracker surrendering as the second beat.
PUNCH_LINE = (
    "I bought a $400 standing desk to fix my posture, "
    "then sat on the floor next to it for 4 hours eating chips "
    "\u2014 my Fitbit gave up and logged it as sleep."
)

MAX_LINE_LENGTH = 200


def checked_line(text):
    """Return the line only if it meets the competition length rules."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("one-liner must not be empty")
    if len(text) != len(stripped):
        raise ValueError("one-liner must not have leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("one-liner must be a single line")
    if len(text) > MAX_LINE_LENGTH:
        raise ValueError(
            f"one-liner is {len(text)} chars, over the {MAX_LINE_LENGTH} limit"
        )
    return text


def main():
    line = checked_line(PUNCH_LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    payload = line.encode("utf-8")
    with open(target, "wb") as handle:
        handle.write(payload)
    digest = hashlib.sha256(payload).hexdigest()
    print(f"wrote {len(payload)} bytes to {target} (sha256 {digest})")


if __name__ == "__main__":
    main()
