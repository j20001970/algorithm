#!/usr/bin/python

count = 0

def hanoi(n, p1, p2, p3):
    global count
    count = count + 1
    if n == 1:
        print("套還從%c移到%c 執行次數: %d" % (p1, p3, count))
    else:
        hanoi(n-1, p1, p3, p2)
        print("套還從%c移到%c 執行次數:%d" % (p1, p3, count))
        hanoi(n-1, p2, p1, p3)

j = int(input("請輸入所移動套環數量: "))
hanoi(j, 'A', 'B', 'C')