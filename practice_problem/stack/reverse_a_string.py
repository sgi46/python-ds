'''
 Problem:
Write a function that reverses a string using a stack (no slicing or built-in reverse).
'''

from src.ds_02_stack.build_stack import Stack 

def reverse_string(org_string):
    rev_string = ""
    stack=Stack()

    for char in org_string:
        stack.push(char)

    for _ in range(len(org_string)):
        rev_string+=stack.pop()

    return rev_string

input_string = 'MADAM'
print(reverse_string(input_string))