"""
Given a string, repeatedly remove adjacent duplicate characters.
remove_duplicates("abbaca") → "ca"  
# 'bb' is removed → "aaca", then 'aa' → "ca"
"""

from src.ds_02_stack.build_stack import Stack

def remove_duplicates(input):
    stack = Stack()

    for char in input:
        print(stack)
        if char==stack.peek():
            stack.pop()
        else:
            stack.push(char)
    return stack.to_string()

print(remove_duplicates("abbaca"))

