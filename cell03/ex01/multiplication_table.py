#!/usr/bin/env python3

print('Enter a number')
multiplier = int(input())

max_ceiling = 10

for i in range(max_ceiling):
	product = i * multiplier
	print(f'{i} x {multiplier} = {product}')
