#!/usr/bin/env python3
import sys

arg = sys.argv[1:]
arg_num = len(arg)

if arg_num == 0:
    print('none')

print(f'parameter: {arg_num}')

for i in arg:
    print(f'{i}: {len(i)}')