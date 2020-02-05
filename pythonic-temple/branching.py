#!/usr/bin/env python3

import sys

assert len(sys.argv) >= 3, print("## Needs at least 2 arguments")

num_list = [int(i) for i in sys.argv[1:]]
arg_sum = sum(num_list)

if arg_sum <= 0:
    print("You have chosen the path of destitution.")
elif arg_sum >= 1 and arg_sum <= 100:
    print("You have chosen the path of plenty.")
else:
    print("You have thosen the path of excess.")
