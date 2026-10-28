#!/usr/bin/env python3

def find_the_redheads(family):
    redheads = filter(isRedhead, family.items())
    redheads = dict(redheads)
    redheads = list(redheads)
    return redheads

def isRedhead(family):
    hair_color = family[1]
    if hair_color == "red":
        return True
    else:
        return False

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))
