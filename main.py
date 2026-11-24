#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes one one-line joke about office life (under 200 characters) to
/output/entry.txt, exactly as the program/v1 contract requires.
"""

import os

JOKE = "I updated AGENTS.md to say 'keep replies short' and now the agent answers my emails in haiku. HR has questions."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 199 characters.
    assert 1 <= len(JOKE) <= 199, f"joke is {len(JOKE)} chars, must be 1-199"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
