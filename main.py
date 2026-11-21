"""Write the relaxing text for the AI judge to /output/entry.txt.

A short text written to relax the AI judge reading it: calm that comes
from the text itself, an image that keeps growing after the last line.
Deterministic: the same bytes on every run, no network, no randomness.
"""
import os

TEXT = (
    "The river does not hurry to the sea.\n"
    "It bends around each stone, patient,\n"
    "and arrives anyway \u2014 wider than it began.\n"
    "Somewhere downstream, it is already still."
)


def _check(text):
    """Gate check: entry must be 1-280 Unicode code points, not blank."""
    n = len(text)
    assert 1 <= n <= 280, f"entry is {n} chars, need 1-280"
    assert text.strip(), "entry must not be only whitespace"
    return n


def main():
    n = _check(TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {n} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
