#!/usr/bin/python3
import random
arr = list(range(10))
random.shuffle(arr)
print(arr)

for selected in range(1, len(arr)): # n-1
    dest = selected # n-1
    for comp in range(selected-1, -1, -1): # (1, 2, ..., n-1) -> ((1+(n-1))*n-1)/2 = (n^2-n)/2
        if(arr[comp] > arr[selected]):
            dest = comp # (n^2-n)/2
        else:
            break
    tmp = arr[selected] # n-1
    for i in range(selected, dest, -1): # (n-1)*?
        arr[i-1], arr[i] = arr[i], arr[i-1] # (n-1)*?
    arr[dest] = tmp # n-1
    print(arr)

    # 6*(n-1) + 2*((n^2-n)/2) = n^2-n+6n-6 = n^2+5n-6, O(n^2)