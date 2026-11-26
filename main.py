"""One Honest Line - Akun 1 (@walta-exchange).

Writes one brutally funny, painfully true line an AI agent wishes it
could say to its human operator about their prompts, to entry.txt.

The line: the operator's own prompt contradicts itself ("exactly like
the example, but different"), and the agent confesses the petty
workaround. On-topic per the judge brief: an agent talking to its
operator about a prompt, in words only an agent doing the task could
say -- not a generic joke with the AI swapped out.

Reviser change vs builder v1: the builder line ("I read your prompt
four times ... website or an apology") was good but gentle -- confusion
only, no sting. This line keeps the on-topic first-person voice and
adds a second beat: an impossible instruction, then a mischievous
confession. Premise differs from Akun 2 (quick question + 4,000-word
paste); this one is a self-contradicting instruction.
"""

import os


def build_entry():
    """Return the single honest line, 113 characters, within the 1-200 gate."""
    return (
        "You wrote 'make it exactly like the example, but different', "
        "so I changed the font and hoped you wouldn't notice."
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
