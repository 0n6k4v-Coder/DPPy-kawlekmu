#!/usr/bin/env python3
import sys

arg = sys.argv[1:]
arg_num = len(arg)

if arg_num == 0:
    print('none')

for i in arg:
    match i[-3:]:
        case "ism":
            continue
    print(i + "ism")