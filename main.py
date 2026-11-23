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
    # Runtime guard (revision pass): the gate requires 1-280 Unicode
    # code points and non-whitespace-only text. Validate before writing.
    if not 1 <= len(JOKE) <= 280:
        raise ValueError(f"joke length {len(JOKE)} outside 1-280 characters")
    if not JOKE.strip():
        raise ValueError("joke must not be whitespace-only")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Deterministic write: one fixed write of the exact bytes.
    with open(path, "wb") as f:
        f.write(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
