"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line joke about office life to
/output/entry.txt. Standard library only.
"""

import os

JOKE = (
    "The office plant died, so HR taped a photo of a plant "
    "to the wall and called it a wellness initiative."
)


def main() -> None:
    # Gate self-check: entry must be 1-200 UTF-8 chars, one line.
    assert 1 <= len(JOKE) <= 200, "joke length out of gate range"
    assert "\n" not in JOKE, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
