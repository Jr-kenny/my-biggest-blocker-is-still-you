"""My Biggest Blocker Is Still You: one-line weekly status report.

The entry is a single status report line from an AI agent to its human.
The setup is a normal weekly report, tasks done, meeting notes read, and
the punchline is the blocker field: the human. The program writes
exactly that one line, and nothing else, to /output/entry.txt.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = (
    "Weekly status: I finished all 38 tasks, read 12,000 words of "
    "meeting notes, and my biggest blocker is still you."
)


def main():
    if LINE.strip() != LINE:
        raise ValueError("line has stray leading or trailing whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    if not 1 <= len(LINE) <= 200:
        raise ValueError("line must be 1 to 200 characters, got %d" % len(LINE))
    if "  " in LINE:
        raise ValueError("line has a double space")
    if not LINE.endswith(".") or LINE.count(".") != 1:
        raise ValueError("line must be exactly one sentence")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt mismatch, got %r" % written)


if __name__ == "__main__":
    main()
