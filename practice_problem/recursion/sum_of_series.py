"""
Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0) using recursion .

Test Data:
sum_series(6) -> 12
sum_series(10) -> 30
"""

def sumSeries(n):
    if n=<0:
        return 0
    return n+sumSeries(n-2)

print(sumSeries(10))