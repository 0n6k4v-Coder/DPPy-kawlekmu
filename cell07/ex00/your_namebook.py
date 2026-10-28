#!/usr/bin/env python3

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

def array_of_names(persons):
    array = []

    for first_name, last_name in persons.items():
        fullname = first_name.capitalize() + " " + last_name.capitalize() 
        array.append(fullname)

    return(array)

print(array_of_names(persons))