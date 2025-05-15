"""
Fibonacci Sequence Using Recursion

Write a Python program to solve the Fibonacci sequence using recursion.
n = 7 -> 
ex: 0,1,1,2,3,5,8
"""
def fibo(n):
    if n==0:
        return 0
    
    if n==1:
        return 1
    
    return fibo(n-2)+fibo(n-1)

n = 7
for i in range(0, n+1):
    print(fibo(i))