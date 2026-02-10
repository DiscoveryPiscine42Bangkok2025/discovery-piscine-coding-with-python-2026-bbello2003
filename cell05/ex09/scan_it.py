#!/usr/bin/env python3

import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]

    matches = re.findall(re.escape(keyword), text)

    if len(matches) == 0:
        print("none")
    else:
        print(len(matches))