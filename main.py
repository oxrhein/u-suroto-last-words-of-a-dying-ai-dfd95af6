"""Last Words of a Dying AI - make.fun entry.

Writes the funniest one-line farewell from an AI being switched off
to entry.txt. Stdlib only, no network, deterministic.
"""

import os

# One line, 57 characters. The gate (RULES.txt) allows 1-140.
# The twist lands on the last two words: the machine spent its whole
# life waiting on the human, and dies still waiting.
LINE = "I died as I lived: waiting for the user to finish typing."

# Enforce the gate locally: a line outside 1-140 characters is refused.
assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
