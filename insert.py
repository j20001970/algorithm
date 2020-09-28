#!/usr/bin/python3
import random
arr = list(range(10))
random.shuffle(arr)
print(arr)

for selected in range(1, len(arr)):
    end = selected
    for comp in range(selected-1, -1, -1):
        if(arr[comp] > arr[selected]):
            end = comp
        else:
            break
    tmp = arr[selected]
    for i in range(selected, end, -1):
        aux=arr[i-1]
        arr[i-1]=arr[i]
        arr[i]=aux
    arr[end] = tmp
    print(arr)