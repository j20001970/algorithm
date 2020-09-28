#!/usr/bin/python3
import random
arr = list(range(10))
random.shuffle(arr)
print(arr)

for dest in range(len(arr)-1):
    selected = dest
    for i in range(dest+1, len(arr)):
        if arr[selected] > arr[i]:
            selected = i
    aux = arr[selected]
    arr[selected]=arr[dest]
    arr[dest] = aux
    print(arr)