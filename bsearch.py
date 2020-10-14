#1/usr/bin/python

data = [5, 8, 9, 15, 30]

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

result = bsearch(data, 9)

if result != None:
    print("found at index %d" % result)
else:
    print("not found")