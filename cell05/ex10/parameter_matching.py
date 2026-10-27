#!/usr/bin/env python3
import sys

arg = sys.argv[1:]
arg_num = len(arg)

if arg_num != 1:
	print('none')
	exit()

arg = arg[0]
word = input('What was the parameter? ')

if arg == word: print('Good job!')
else: print('Nope, sorry...')