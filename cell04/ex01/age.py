#!/usr/bin/env python3

decades = [10, 20, 30]
current_age = int(input("Please tell me your age: "))

for decade in decades:
	next_decade_age = current_age + decade
	print(f"In {decade} years, you'll be {next_decade_age} years old.")
