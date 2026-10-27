#!/usr/bin/env python3

def array_of_names(persons):
    array = []

    for i in persons:
        first_name = i[0].upper() + i[1:]
        last_name = persons[i][0].upper() + persons[i][1:]

        fullname = first_name + " " + last_name
        array.append(fullname)

    return(array)

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))