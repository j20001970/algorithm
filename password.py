#!/usr/bin/python

import random

MIN = 1
MAX = 100
ans = random.randint(MIN, MAX)
print(ans)

lb = MIN
rb = MAX
while True:
    user_input = input("密碼介於 %d-%d" % (lb, rb))
    if not user_input.isdigit():
        continue
    user_input = float(user_input)
    if user_input == ans:
        print("答對了！")
        break
    if user_input < ans:
        lb = user_input
    elif user_input > ans:
        rb = user_input