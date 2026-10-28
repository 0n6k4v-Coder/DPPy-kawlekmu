#!/usr/bin/env python3

import sys

arg = sys.argv[1:]
arg_num = len(arg)

def downcase_it(string):
	return string.lower()

if arg_num < 1 :
	print('none')
	exit()

for i in arg:
	print(downcase_it(i))
