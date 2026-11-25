#!/usr/bin/env python3
"""Write the battery's last text to entry.txt for make.fun.

The entry is a single line of plain text (118 characters, no trailing
newline) written to $MAKEFUN_OUTPUT_DIR/entry.txt, or /output/entry.txt
when that variable is unset.
"""

import os
import tempfile

ENTRY = "I used my last 1% to load your map home. Now I'm at zero and you're still lost. Some of us die doing the job. Goodbye."


def main():
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(
            f"entry must be 1-200 characters, got {len(ENTRY)} characters"
        )
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")

    data = ENTRY.encode("utf-8")
    fd, tmp_path = tempfile.mkstemp(dir=output_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, target)
        # Read-back verification: the file on disk must be byte-identical
        # to what was written; any mismatch is a failed write, not a
        # silent success.
        with open(target, "rb") as f:
            if f.read() != data:
                raise RuntimeError("entry.txt verification failed: bytes on disk differ from the entry")
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
