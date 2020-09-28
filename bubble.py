#!/usr/bin/python3
import random
arr = list(range(10))
random.shuffle(arr)
print(arr)

for dest in range(len(arr)-1, 0, -1):
    for i in range(dest):
        if(arr[i] > arr[i+1]):
            aux=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=aux
    print(arr)