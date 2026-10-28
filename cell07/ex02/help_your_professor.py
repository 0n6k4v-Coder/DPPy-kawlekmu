#!/usr/bin/env python3

def average(item):
    summm = sum(item.values())
    total = len(item)
    average = summm / total
    return average

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f'{average(class_3B)}')
print(f'{average(class_3C)}')