"""
Sum of List Using Recursion

Write a Python program to calculate the sum of a list of numbers using recursion.

"""

def rec_sum(arr):
    if len(arr)==1:
        return arr[0]
    return arr[-1]+sum(arr[:-1])

print(rec_sum([3, 5, 2, 10]))
