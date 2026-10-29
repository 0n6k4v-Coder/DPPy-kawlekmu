#!/usr/bin/env python3

def famous_births(women_scientists):
    sorted_women_scientists = dict(
        sorted(
            women_scientists.items(),
            key=lambda item: int(item[1]["date_of_birth"])
        )
    )

    for scientist in sorted_women_scientists:
        scientist = sorted_women_scientists[scientist]

        scientist_name = scientist["name"]
        scientist_dob = scientist["date_of_birth"]

        print(f'{scientist_name} is a great scientist born in {scientist_dob}.')


women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)