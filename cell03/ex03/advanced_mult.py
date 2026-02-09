#!/usr/bin/env python3

import sys

if len(sys.argv) != 1:
    print("none")
    sys.exit(0)

i = 0
while i <= 10:
    j = 0
    line = "Table de " + str(i) + ":"
    while j <= 10:
        line += " " + str(i * j)
        j += 1
    print(line)
    i += 1