"""
Problem:
Given a sorted array of integers and a target value, find if there exists a pair of numbers that 
add up to the target and returns its index.

Example:
arr = [1, 2, 3, 4, 6], target = 6
Return: (1, 3) because 2 + 4 = 6
"""

def two_sum(arr, target):
    start = 0 
    end = len(arr)-1

    while start<end:
        sum = arr[start]+arr[end]
        if sum == target:
            return (start, end)
        elif sum>target:
            end-=1
        else:
            start+=1

    return "No pair found"

print(two_sum([1, 2, 3, 4, 6], 100))
