#!/usr/bin/env python3
import sys

arg = sys.argv[1:]
arg_num = len(arg)

if arg_num != 2:
        print("none")
        exit()

array = []

first_argv = int(arg[0])
second_argv = int(arg[1])

for i in range(first_argv, second_argv + 1):
	array.append(i)

print(array)
