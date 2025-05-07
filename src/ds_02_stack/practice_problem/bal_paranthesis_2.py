"""
In a string with characters *, (, and ), the * can act as either (, ), or be an empty string. 
Write a function to check if the string is valid.
check_valid("(*)") → True  
check_valid("(*))") → True
"""

from src.ds_02_stack.build_stack import Stack

def check_valid(input):
    d = {
        '[':']',
        '{':'}',
        '(': [')','*']
    }

    stack=Stack()

    for char in input:
        if char in d:
            stack.push(char)
        elif stack.size()!=0 or char not in d[stack.pop()]:
            return False
    return stack.size() == 0

print(check_valid("*("))

