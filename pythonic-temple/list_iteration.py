#!/usr/bin/env python3

import sys

for i, name in enumerate(sys.argv[1:]):
    print(f"{i+1}. {name}")
