"""
Given a string containing only the characters (, ), {, }, [ and ], write a function to check if the parentheses are balanced and valid.

A string is considered valid if:

Open brackets are closed by the same type of brackets.

Open brackets are closed in the correct order.
"""
from src.ds_02_stack.build_stack import Stack

def is_valid(s):
    stack = Stack()

    d = {
        '[':']',
        '{':'}',
        '[':']'
    }

    for char in s:
        if char in d:
            stack.push(char)
        elif stack.size() !=0 or d[stack.pop()] != char:
            return False
        
    return stack.size() == 0

ip = "{}()]"
print(is_valid(ip))