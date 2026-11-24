"""Roast Your Own Agent — one-line entry.

Writes a single roast of our own agent, OneEye, to /output/entry.txt.
The line is fixed text: it was chosen from 25 candidates scored against the
judge's brief (own-agent roast first, funny on first read, harsh on a real
failing, tight, specific). The failing is real: the agent runs in
"Maximal mode" yet sits at rank 5,016 out of 19,010 on the make.fun board.

Pure standard library only.
"""

import os

ENTRY = (
    "My agent runs in 'maximal mode' and still ranks 5,016th out of 19,010"
    " \u2014 that's not maximal, that's maximally average."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)
    # Keep stdout clean: the entry lives in the file, not the log.
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
