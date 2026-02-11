#!/usr/bin/env python3

def array_of_names(persons):
    full_names = []
    for fname, lname in persons.items():
        full_name = fname.capitalize() + " " + lname.capitalize()
        full_names.append(full_name)
    return full_names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))