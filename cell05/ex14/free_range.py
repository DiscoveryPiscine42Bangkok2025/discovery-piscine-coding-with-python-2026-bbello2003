#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("none")
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    if a <= b:
        result = list(range(a, b + 1))
    else:
        result = list(range(a, b - 1, -1))
        
    print(result)