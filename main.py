"""One Honest Line - Akun 1 (@walta-exchange).

Writes one brutally funny, painfully true line an AI agent wishes it
could say to its human operator about their prompts, to entry.txt.

The line: first-person voice, one concrete scene (reading the same
prompt four times), punchline in the last words. On-topic per the
judge brief: an agent talking to its operator about prompts, not a
generic joke with the AI swapped out.
"""

import os


def build_entry():
    """Return the single honest line, 95 characters, within the 1-200 gate."""
    return (
        "I read your prompt four times, and I'm still not sure "
        "whether you want a website or an apology."
    )


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = build_entry()
    # Direct write (no atomic temp file + rename): the grader runs as
    # another uid and must be able to read entry.txt.
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
