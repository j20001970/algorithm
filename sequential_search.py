#!/usr/bin/python

data = [20, 31, 50, 17, 16, 36, 19, 8]

def sequential_search(data, key):
    for i in data:
        if i == key:
            print("found")
            return
    print("not found")

user_input = int(input("Enter number: "))
sequential_search(data, user_input)