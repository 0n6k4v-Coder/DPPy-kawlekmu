#!/usr/bin/env python3
import sys

params = sys.argv[1:3]
params_num = len(params)

if params_num != 2:
	print('none')
	exit()

keyword = params[0]
string = params[1]

keyword_num = string.count(keyword)
print(keyword_num)
