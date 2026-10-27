#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
        print("none")
        exit()

array = []

first_argv = int(sys.argv[1])
second_argv = int(sys.argv[2])

for i in range(first_argv, second_argv + 1):
	array.append(i)

print(array)
