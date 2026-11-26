#!/usr/bin/env python3
"""Write one funny line pitching the worst pizza topping to /output/entry.txt.

Deterministic, offline, stdlib only. Honors the ENTRY_OUTPUT_DIR
environment variable, defaulting to /output. The line is written with
no trailing newline.
"""

import os
from pathlib import Path

LINE = (
    "Try our new pizza topped with gas-station sushi: every slice comes with "
    "a free stomach pump, because that salmon has been sunbathing in the "
    "display case since Tuesday."
)


def main() -> None:
    assert 0 < len(LINE) <= 200, "entry line must fit the 200-character cap"
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
