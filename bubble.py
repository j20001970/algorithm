#!/usr/bin/python3
# import random
# arr = list(range(10))
# random.shuffle(arr)

arr = []
for i in range(6):
    while(True):
        user_input = input("enter %d: " % (i))
        if user_input.isdigit():
            arr.append(int(user_input))
            break
        else:
            print(user_input, "is not digit")
print(arr)

for dest in range(len(arr)-1, 0, -1):
    for i in range(dest):
        if(arr[i] > arr[i+1]):
            aux=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=aux
    print(arr)