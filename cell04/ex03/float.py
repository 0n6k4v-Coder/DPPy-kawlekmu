#!/usr/bin/env python3

number =  float(input('Give me a number: '))

match number.is_integer():
	case True:
		print("This number is an integer.")
	case False:
		print("This number is a decimal.")
