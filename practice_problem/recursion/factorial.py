"""
Factorial Using Recursion

Write a Python program to get the factorial of a non-negative integer using recursion.
3! = 1*2*3
"""

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print(fact(4))