#!/usr/bin/env python3

import sys

params = sys.argv[1:]
params_num = len(params)

if (params_num < 2):
	print('none')
	exit()

for string in reversed(params):
	print(string)
