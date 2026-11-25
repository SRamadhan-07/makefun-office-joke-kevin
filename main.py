"""Write the office joke entry for make.fun.

Competition: The Funniest Office Joke, Judged Head to Head.
The program writes a single short line about office life to
/output/entry.txt, exactly as the program/v1 harness expects.
"""

from pathlib import Path

ENTRY_TEXT = (
    "Our standup is fifteen minutes because any longer and the "
    "blockers start naming names \u2014 last week they named the calendar."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate expects UTF-8 text, 1 to 200 characters, on a single line.
    # Write the joke exactly once, with no trailing newline added.
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
