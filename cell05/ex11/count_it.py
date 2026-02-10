#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("none")
else:
    params = sys.argv[1:]
    print(f"parameters: {len(params)}")
    
    for p in params:
        print(f"{p}: {len(p)}")