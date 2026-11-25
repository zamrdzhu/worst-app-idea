#!/usr/bin/env python3
"""Write one worst-app-idea pitch to /output/entry.txt.

The pitch is a single sentence, at most 240 characters, for the
worst, most useless app imaginable: an app that solves nothing and
actively makes your life worse, with a premium tier that makes it
worse still. The uselessness is the joke: the app's only feature
is betraying you at your weakest hour, and paying more only
widens the blast radius to your mother.
"""

import os

LINE = (
    "An app that texts your ex every time you open the fridge after "
    "midnight, with a premium tier that CCs your mom."
)

MAX_CHARS = 240


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "no leading or trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
