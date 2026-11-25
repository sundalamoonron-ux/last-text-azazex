"""Last Text at One Percent — entry for make.fun competition
u-azazex-last-text-at-one-percent-ba9fc876.

Writes the chosen final text message (the dying phone's own voice at 1%
battery) to /output/entry.txt. The gate requires 1-200 UTF-8 characters.
"""

import os
from pathlib import Path

# The winning line: picked after a 10-candidate internal pairwise tournament
# (see candidates.md). C9 went 3-0 against the other finalists.
MESSAGE = (
    "i forgive you for the toilet incident. "
    "i do NOT forgive the 47 open tabs. "
    "delete my history. 1% and out."
)


def main() -> None:
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(MESSAGE, encoding="utf-8")
    print(f"Wrote {len(MESSAGE)} characters to {output_path}")


if __name__ == "__main__":
    main()
