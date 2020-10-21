#!/usr/bin/python

import random
INDEXBOX = 10
MAXNUM = 7
def print_data(data, max_number):
    print('\t', end='')
    for i in range(max_number):
        print('[%2d]' % data[i], end='')
    print("")

def create_table(num, index):
    tmp = num % INDEXBOX
    while True:
        if index[tmp] == -1:
            index[tmp] = num
            break
        else:
            tmp = (tmp+1) % INDEXBOX

def create_table_quadratic(num, index):
    tmp = num % INDEXBOX
    first_tmp = tmp
    collision = 0
    while True:
        if index[tmp] == -1:
            index[tmp] = num
            break
        else:
            collision += 1
            tmp = (first_tmp + collision**2) % INDEXBOX

def create_table_rehash(num, index):
    tmp = num % INDEXBOX
    collision = 0
    while True:
        if index[tmp] == -1:
            index[tmp] = num
            break
        else:
            print("collision")
            collision += 1
            tmp = (num + collision*3) % INDEXBOX

index=[None]*INDEXBOX
data=[None]*MAXNUM

print("原始陣列值: ")
for i in range(MAXNUM):
    data[i]=random.randint(1, 20)
for i in range(INDEXBOX):
    index[i] = -1
print_data(data, MAXNUM)

print("雜湊表內容: ")
for i in range(MAXNUM):
    create_table_rehash(data[i], index)
    print("  %2d =>" % data[i], end='')
    print_data(index, INDEXBOX)

print("完成雜湊表: ")
print_data(index, INDEXBOX)