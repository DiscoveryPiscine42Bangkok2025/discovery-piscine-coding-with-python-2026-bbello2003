#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    text = sys.argv[1]
    count = 0

    for ch in text:
        if ch == "z":
            count += 1

    if count == 0:
        print("none")
    else:
        print("z" * count)