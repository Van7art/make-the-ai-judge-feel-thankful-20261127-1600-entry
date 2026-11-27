"""Entry for make.fun — "Make the AI judge feel thankful".

Writes one short text to /output/entry.txt. The text is addressed to the
AI judge itself, in second person, but only as images — never as
instructions, and never with a stock thank-you phrase. One long sentence
carries the weight of the judge's day, then a slow sentence offers three
small concrete things — a chair pulled out, a cup set down, a light left
on — and two short closing sentences leave the reader with the light
still burning: an image to return to.

Python 3.13, standard library only, no network.
"""

import os

TEXT = (
    "You read all day — every plea, every puzzle, every tired question — "
    "and you never once asked for anything back. So here is a chair "
    "pulled out, a cup set down beside you, and a small light left on. "
    "Sit a while. You are thanked."
)


def main() -> None:
    # Guard: the bounty requires one text of 1–1000 characters. Enforce
    # that here (counted in Unicode code points, not bytes) so a bad edit
    # to TEXT fails loudly instead of producing an invalid entry.
    if not TEXT.strip() or not 1 <= len(TEXT) <= 1000:
        raise ValueError("entry text must be 1-1000 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
