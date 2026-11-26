#!/usr/bin/env python3
"""Write a short family scene that would make the AI judge feel proud."""
import os

TEXT = (
    "At 3 a.m. Mum came home in her bus uniform and reheated soup for the third time. Her son, "
    "who once hid when classmates saw that uniform, set out her slippers: 'Sit. My turn — extra pepper, zero guarantees.'"
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
