"""Loading Screen Gold: A Tip in 200 Characters.

Writes exactly one loading-screen tip (138 characters, one line, no
trailing newline) to <OUTPUT_DIR>/entry.txt.
"""

import os
import tempfile

ENTRY = "Tip: your agent just opened a second terminal to ask itself for help \u2014 two agents are now stuck on the same bug, and both are billing you."


def main() -> None:
    assert "\n" not in ENTRY, "entry must be a single line"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Atomic write: write to a temp file in the same directory, then
    # replace, so a reader never sees a partial entry.txt.
    fd, tmp_path = tempfile.mkstemp(dir=output_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
        os.replace(tmp_path, path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except FileNotFoundError:
            pass
        raise


if __name__ == "__main__":
    main()
