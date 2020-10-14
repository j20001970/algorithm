#1/usr/bin/python

def insert_sort(arr):
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
    return arr

def bsearch(data, key, l=None, r=None):
    l = 0 if l == None else l
    r = len(data) if r == None else r
    if l >= r:
        return None
    m = int((l + r)/2)
    if data[m] < key:
        return bsearch(data, key, m+1, r)
    elif data[m] > key:
        return bsearch(data, key, l, m)
    else:
        return m

data = input("Enter 5 number separated with space: ")
data = data.split(" ")[:5]
for i, d in enumerate(data):
    data[i] = int(d)

print("排序前", data)

data = insert_sort(data)
print("排序後", data)

user_input = int(input("Enter a number to search: "))
result = bsearch(data, user_input)

if result != None:
    print("found at index %d" % result)
else:
    print("not found")