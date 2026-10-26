#!/usr/bin/env python3
import sys

row = 0

if len(sys.argv) > 1:
	print("none")

while(row <= 10):
	column = 0
	result = 0

	print(f'Table de {row}: ', end="")

	while (column <= 10):
		print(f' {result}', end="")
		result += row
		column += 1

	print()
	row += 1
