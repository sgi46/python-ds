"""
Problem:
Given a character array, reverse it in-place.
ex: arr = ['h','e','l','l','o']

return ['o','l','l','e','h']
"""

def reve(arr):
    left = 0
    right = len(arr)-1

    while left<right:
        arr[left], arr[right]=arr[right], arr[left]
        left+=1
        right-=1
    
    return arr

print(reve(['h','e','l','l','o']))