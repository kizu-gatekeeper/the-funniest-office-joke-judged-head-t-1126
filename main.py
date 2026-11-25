"""Entry for make.fun bounty: The Funniest Office Joke, Judged Head to Head.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import sys

LINE = "My boss said the meeting could have been an email, so I sent the email — now we have a meeting to discuss why nobody read it."
MAX_CHARS = 200


def write_entry(out_dir):
    """Validate the entry line and write it with no trailing newline."""
    if not LINE or LINE != LINE.strip() or "\n" in LINE or len(LINE) > MAX_CHARS:
        raise ValueError("entry line fails format validation")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(out_dir)
    print(f"wrote {path} ({len(LINE)} chars)")


if __name__ == "__main__":
    sys.exit(main())
