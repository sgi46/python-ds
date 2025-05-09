"""
Problem:
Given a sorted array, remove duplicates in-place and return the length of the new array without duplicates.

Example:
arr = [1, 1, 2, 3, 3]
Return: 3 and array becomes [1, 2, 3]
"""

# def rem_dup(arr):
#     pointer_1=len(arr)-1
#     pointer_2=len(arr)-2

#     # for _ in range(len(arr)-1, -1, -1):
#     while pointer_2>=0:
#         if arr[pointer_1]==arr[pointer_2]:
#             arr.pop(pointer_1)
#             pointer_2-=1
#             pointer_1-=1
#         else:
#             pointer_1-=1
#             pointer_2-=1
    
#     return arr

def remove_duplicates(arr):
    if not arr:
        return 0

    write = 1  # index to write the next unique element

    for read in range(1, len(arr)):
        if arr[read] != arr[read - 1]:
            arr[write] = arr[read]
            write += 1

    return arr[:write]  # return the deduplicated array


print(remove_duplicates([1, 1, 2, 3, 3]))
