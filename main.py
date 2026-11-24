"""Funniest Time Machine Warning Label entry (Python 3.13, stdlib only).

Writes a single warning label, 120 characters at most, to entry.txt in
the output directory and reads it back to prove the bytes landed.
"""

import os
from pathlib import Path

LABEL = (
    "WARNING: Do not kill your grandfather. "
    "HR has no form for that, and you would not exist to file it."
)

MAX_CHARS = 120


def output_path() -> Path:
    """Where the grader reads the entry: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def write_entry() -> Path:
    """Write the label, then read it back and verify it in full."""
    text = LABEL.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"label is {len(text)} chars, must be 1-{MAX_CHARS}")
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    written = target.read_text(encoding="utf-8")
    if written != text:
        raise IOError("read-back text does not match the label")
    # Byte-exact read-back: the gate counts characters, the judge reads
    # bytes, so both must match the label exactly.
    if target.read_bytes() != text.encode("utf-8"):
        raise IOError("read-back bytes do not match the label")
    return target


def main() -> None:
    target = write_entry()
    print(f"wrote {target} ({len(LABEL.strip())} chars)")


if __name__ == "__main__":
    main()
