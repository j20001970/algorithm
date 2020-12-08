#!/usr/bin/python3
from collections import namedtuple
t = [25, 20, 5, 1]

def change_greed(t, n):
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):
        if n >= money:
            m[i] = n // money
            n = n % money
            print(m, n)
    return m, n

def change_dp(coins, n):
    m = [[0 for _ in range(n+1)] for _ in range(len(t)+1)]
    for i in range(1, n+1):
        m[0][i] = float('inf')
    for c in range(1, len(coins) + 1):
        for r in range(1, n + 1):
            # Just use the coin coins[c - 1].
            if coins[c - 1] == r:
                m[c][r] = 1
            # coins[c - 1] cannot be included.
            # Use the previous solution for making r,
            # excluding coins[c - 1].
            elif coins[c - 1] > r:
                m[c][r] = m[c - 1][r]
            # coins[c - 1] can be used.
            # Decide which one of the following solutions is the best:
            # 1. Using the previous solution for making r (without using coins[c - 1]).
            # 2. Using the previous solution for making r - coins[c - 1] (without
            #      using coins[c - 1]) plus this 1 extra coin.
            else:
                m[c][r] = min(m[c - 1][r], 1 + m[c][r - coins[c - 1]])
    return m[-1][-1]

item = namedtuple("Item", ['name', 'weight', 'value'])
items = [item("PS5", 5, 17000), item("iPad Pro 12", 1, 35000), item("Macbook pro 15", 4, 60000), item("HomePod", 3, 9000), item("Mac mini", 2, 20000)]

def knapsack_greed(items):
    weight = 10
    bag = []
    items.sort(key=lambda key : key.value, reverse=True)
    for item in items:
        if not weight:
            break
        if (weight-item.weight)>=0:
            weight -= item.weight
            bag.append(item)
    print("背包有: ")
    value = 0
    for i in bag:
        print("Name=%s, Weight=%d, Value=%d"%(i.name, i.weight, i.value))
        value += i.value
    print("Total value: %d"%value)

def knapsack_dp(W, items, n): 
  
    # Base Case 
    if n == 0 or W == 0: 
        return 0
  
    # If weight of the nth item is 
    # more than Knapsack of capacity W, 
    # then this item cannot be included 
    # in the optimal solution 
    if (items[n-1].weight > W): 
        return knapsack_dp(W, items, n-1)
  
    # return the maximum of two cases: 
    # (1) nth item included 
    # (2) not included 
    else: 
        return max( 
            items[n-1].value + knapsack_dp( 
                W-items[n-1].weight, items, n-1), 
            knapsack_dp(W, items, n-1)) 

change_greed(t, 41)
print(change_dp(t, 41))

knapsack_greed(items)
print(knapsack_dp(10, items, len(items)))