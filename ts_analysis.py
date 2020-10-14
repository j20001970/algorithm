#!/usr/bin/python3

# Time & Space Complexity: 找質數

prime_table = [
    False, False, True, True, False, True, False, True, False, False, 
    False, True, False, True, False, False, False, True, False, True, 
    False, False, False, True, False, False, False, False, False, True, 
    False, True, False, False, False, False, False, True, False, False, 
    False, True, False, True, False, False, False, True, False, False, 
    False, False, False, True, False, False, False, False, False, True, 
    False, True, False, False, False, False, False, True, False, False, 
    False, True, False, True, False, False, False, False, False, True, 
    False, False, False, True, False, False, False, False, False, True, 
    False, False, False, False, False, False, False, True, False, False
]

def time(n):
    if n in [0, 1]: # 1
        return False # 1
    for i in range(2, int(n**0.5)+1): # n^0.5-1
        if n % i == 0: # n^0.5-1
            return False # 1
    return True # 1
    # 2*(n^0.5-1)+4 = 2*(n^0.5)+2, O(sqrt(n))

def space(n):
    try:
        return prime_table[n] # 1
        # 1, O(1)
    except Exception as e:
        print(e)
        return None
