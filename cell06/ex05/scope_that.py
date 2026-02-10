#!/usr/bin/env python3

def add_one(n):
    n += 1
    print("inside function >>>", n)

number = 5
print("before function call >>>", number)
add_one(number)
print("after function call >>>", number)