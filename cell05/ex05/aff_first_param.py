#!/usr/bin/env python3
import sys

arg = sys.argv[1:]
arg_num = len(arg)

if (arg_num < 1):
	print("none")
	exit()

if arg: print(arg[0])
