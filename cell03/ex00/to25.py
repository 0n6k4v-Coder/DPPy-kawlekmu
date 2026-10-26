#!/usr/bin/env python3

iteration = int(input())
max_iteration = 25

if (iteration > max_iteration):
	print("Error")
	exit()

while (iteration <= max_iteration):
	print(f'Inside the loop, my variable is {iteration}')
	iteration += 1
