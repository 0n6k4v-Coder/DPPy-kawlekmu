#!/usr/bin/env python3

print("Enter the first number:")
first_number = int(input())

print("Enter the second number:")
second_number = int(input())

product = first_number * second_number
print(f'{first_number} x {second_number} = {product}')

if (product > 0):
	print("The result is positive.")
if (product < 0):
	print("The result is negative.")
if (product == 0):
	print("The result is positive and negative.")
