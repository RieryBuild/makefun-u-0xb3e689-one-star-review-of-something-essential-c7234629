"""The fridge never asked for my socks, yet gravity keeps delivering them there."""

import os

REVIEW = "One star. Gravity puts everything I drop under the fridge, including things the fridge did not need."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")  # one file, one review, no extras
    with open(target, "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
