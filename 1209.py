#!/usr/bin/python

def split_number(n, maxsize=None):
    if maxsize == None:
        maxsize = n
    if n == 1:
        return [1]
    if n > maxsize:
        return [1]*n
    ret = []
    for i in range(n, 0, -1):
        if i == n:
            ret.append([i])
        else:
            e = split_number(n-i, i)
            if type(e[0]) == type([]):
                for j in e:
                    p2 = [i]
                    p2.extend(j)
                    ret.append(p2)
            else:
                p = [i]
                p.extend(e)
                ret.append(p)
    return ret

def sum(a):
    sum = 0
    for i in a:
        sum += price_table[i]
    return sum

price_table = [0, 1, 5, 8, 8, 10, 17, 17, 20, 24, 30]

split = split_number(7)
values = list(map(sum, split))
print(max(values))