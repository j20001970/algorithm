#!/usr/bin/python3
import random

def insertion(arr):
    print("插入排序")
    # 從第1個element選到最後一個
    for selected in range(1, len(arr)):
        # 目的位置索引dest, 先設為原selected位置
        dest = selected
        # 比較數值索引comp從selected-1的位置往前數
        for comp in range(selected-1, -1, -1):
            # 如果arr[comp]比arr[selected]大就設dest為comp
            if(arr[comp] > arr[selected]):
                dest = comp
            else:
                break
        # 把要做插入的數值存入暫存
        tmp = arr[selected]
        # 從selected往前數到dest之前
        for i in range(selected, dest, -1):
            # 把i-1的值往後移到i
            arr[i] = arr[i-1]
        # 把目的索引的值設為tmp
        arr[dest] = tmp
        print("第%d次排序:" % selected, arr)

def selection(arr):
    print("選擇排序")
    # 目的索引從0數到倒數第2個, 因為最後一個位置不用排
    for dest in range(len(arr)-1):
        # 被選中要跟dest的值交換位置的索引, 先設為跟dest一樣
        selected = dest
        # 從dest的下一個位置開始數到最後, 找到範圍中最大的值
        for i in range(dest+1, len(arr)):
            # 如果arr[i]的值比被選中的大, 將selected設為i
            if arr[selected] < arr[i]:
                selected = i
        # 現在selected是範圍中最大的值, 跟dest位置的值交換
        arr[selected], arr[dest] = arr[dest], arr[selected]
        print("第%d次排序:" % int(dest+1), arr)

arr = []
for i in range(8):
    arr.append(random.randint(0, 100))
print("原始數列:", arr)
print()
insertion(arr.copy())
print()
selection(arr.copy())
