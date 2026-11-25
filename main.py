"""One Emoji, One Smile — entry for karwizinudin.

The judge is a warmth judge: it picks the emoji most likely to make a
stranger smile, weighing warmth at first glance, universality, and
whether the pick feels chosen rather than default.

Candidates considered (each scored 1-5 on warmth, universality, chosen):
  - :) plain smiley: warm 3, universal 5, chosen 1 -> too default.
  - 🌞 sun: warm 4, universal 4, chosen 3 -> cheerful but not a face.
  - 🫶 heart hands: warm 4, universal 3, chosen 4 -> intimate for a stranger.
  - 🤗 hugging face: warm 5, universal 5, chosen 4 -> a hug from a
    stranger reads as open arms, instantly friendly, no irony, no
    in-joke. Best total, so it is the pick.
"""

import os

EMOJI = "🤗"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    # Self-check: the gate wants UTF-8 text of 1-8 chars, not only
    # whitespace. Fail loudly here rather than shipping a bad file.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert 1 <= len(written) <= 8, f"bad entry length: {len(written)}"
    assert written.strip(), "entry is only whitespace"
    assert written == EMOJI, "entry does not match the chosen emoji"


if __name__ == "__main__":
    main()
