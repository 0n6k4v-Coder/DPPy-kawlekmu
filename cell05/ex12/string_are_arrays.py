#!/usr/bin/env python3

import sys

arg = sys.argv[1:2]
arg_num = len(arg)

if (arg_num != 1) or (arg[0].count("z")) == 0:
    print('none')
    exit()

for i in arg[0]:
    if (i == "z"): print(i, end="")