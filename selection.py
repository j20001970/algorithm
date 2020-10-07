#!/usr/bin/python3
import random
arr = list(range(10))
random.shuffle(arr)
print(arr)

for dest in range(len(arr)-1): # n-1
    selected = dest # n-1
    for i in range(dest+1, len(arr)): # (n-1, n-2, ..., n-(n-1)) -> ((1+n-1)*(n-1))/2 = (n^2-n)/2
        if arr[selected] > arr[i]:
            selected = i # (n^2-n)/2
    arr[selected], arr[dest] = arr[dest], arr[selected] # n-1
    print(arr)

    # 3*(n-1) + 2*((n^2-n)/2) = n^2-n+3n-3 = n^2+2n-3, O(n^2)