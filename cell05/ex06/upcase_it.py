#!/usr/bin/env python3
import sys

param = sys.argv[1:]
param_num = len(param)

if param_num != 1:
	print('none')
	exit()

print(param[0].upper())
