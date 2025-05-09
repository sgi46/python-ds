"""
Given an array, for each element, find the next greater element to its right. 
If there is none, use -1.
Input:  [4, 5, 2, 25]
Output: [5, 25, 25, -1]
"""

from src.ds_02_stack.build_stack import Stack

def find_greater_ele(elements):
    ans = [-1]*len(elements)
    stack = []
    
    for i, ele in enumerate(elements):
        while stack and ele>elements[stack[-1]]:
            prev_index = stack.pop()
            ans[prev_index] = ele
        stack.append(i)

    return ans

print(find_greater_ele([4, 5, 2, 25]))
# ans -> 0