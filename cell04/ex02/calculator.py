#!/usr/bin/env python3
import operator

operators = {
	"+": operator.add,
	"-": operator.sub,
	"/": operator.truediv,
	"*": operator.mul
}

first_number = int(input("Give me the first number: "))
second_number = int(input("Give me the second number: "))

print("Thank you!")

for operator in operators:
	result = operators[operator](first_number, second_number)
	print(f'{first_number} {operator} {second_number} = {int(result)}')
