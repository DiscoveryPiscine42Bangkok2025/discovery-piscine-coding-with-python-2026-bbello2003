#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    answer = input("What was the parameter? ")
    if answer == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")