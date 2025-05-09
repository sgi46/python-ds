"""
 Problem Summary:
Given an array height[], where each value represents the height of a vertical line on the x-axis, 
find the two lines that, together with the x-axis, form a container that holds the most water.

Ex:
arr = [1,8,6,2,5,4,8,3,7]

Return: 49 — between heights 8 and 7

"""
def container(arr):
    left = 0
    right = len(arr)-1
   
    max_area = 0
    while(left<right):
        current_area = min(arr[left], arr[right])*(right-left)
        max_area=max(current_area, max_area)
        if arr[left]<arr[right]:
            left+=1
        else:
            right-=1

    return max_area

print(container([1,8,6,2,5,4,8,3,7]))