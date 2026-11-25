"""The Funniest Sick-Day Excuse — make.fun entry.

The entry (one line, under 200 characters):

    I sneezed so hard my back filed for workers' comp, so I'm staying
    horizontal until further notice.

Why this line, against the judge brief:

1. Half believable, big laugh: hurting your back from a sneeze is a real,
   documented thing, so a boss can half believe it — while the image of a
   back filing paperwork is absurd enough for a coworker to laugh at.
2. Fresh idea: no fever, no dog, no dead grandmother. The joke is built on
   bureaucratic personification (a body part filing a claim), not a worn
   excuse template.
3. Twist near the end: "filed for workers' comp" lands just past the middle
   and "staying horizontal until further notice" closes on the punchline's
   consequence — the laugh arrives before the last word.
4. Sounds like a real person typing a message: first person, plain words,
   no setup-punchline scaffolding, no joke-book phrasing.
5. No wasted words: every clause does work — the sneeze (cause), the claim
   (joke), the horizontal day off (the ask).
"""

import os

ENTRY = (
    "I sneezed so hard my back filed for workers' comp, "
    "so I'm staying horizontal until further notice."
)


def main() -> None:
    # The sealed scorer requires 1-200 characters of UTF-8 text, not only
    # whitespace: enforce the gate here so a bad line can never ship.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # make.fun collects outputs as a different user than the program runs
    # as, so the file must be readable by everyone (mode 0644).
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
