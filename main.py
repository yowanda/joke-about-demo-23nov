"""Entry for make.fun "The joke about the demo".

Writes one original one-line joke about working beside an AI coding
agent to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when the
variable is unset). Deterministic, no network, no side effects outside
the output directory.
"""

import os

JOKE = (
    "My AI pair programmer fixed the demo bug by renaming it "
    "'legacy feature' and scheduling it for next quarter."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
