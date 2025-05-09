"""
Problem:
Given an array, find all unique triplets that sum up to zero.

Ex: arr = [-1, 0, 1, 2, -1, -4]
[[-1, -1, 2], [-1, 0, 1]]
"""

def triplets(arr):
    arr.sort()
    res = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        j=i+1
        k=len(arr)-1
        
        while j<k:
            current_sum = arr[i]+arr[j]+arr[k]
            if current_sum>0:
                k-=1
            elif current_sum<0:
                j+=1
            else:
                res.append((arr[i], arr[j], arr[k]))
                j+=1
                k-=1

            while j<k and arr[j]==arr[j+1]:
                k+=1
        
    return res

print(triplets([-1, 0, 1, 2, -1, -4]))

