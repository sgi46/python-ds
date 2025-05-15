"""
Write a Python program to sum recursion lists using recursion.

Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21
"""

def sum_using_recursion(arr):
    if not arr:
        return 0
    if isinstance(arr[0], list):
        return sum_using_recursion(arr[0])+sum_using_recursion(arr[1:])
    else:
        return arr[0]+sum_using_recursion(arr[1:])

print(sum_using_recursion([1, 2, [3,4], [5,6]]))
    