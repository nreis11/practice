"""https://leetcode.com/problems/"""

def move_zeroes(n):
    for i in n:
        if i == 0:
            n.remove(0)
            n.append(0)

def add_digits(num):
    
