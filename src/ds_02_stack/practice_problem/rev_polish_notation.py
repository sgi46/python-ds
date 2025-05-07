"""
Evaluate a postfix expression using stack.
tokens = ["2", "1", "+", "3", "*"]
# → ((2 + 1) * 3) = 9
"""

import re
from src.ds_02_stack.build_stack import Stack

# def rpn(tokens):
#     stack=Stack()
#     res = ""
#     for item in tokens:
#         if item in ["+", "-", "/", "*"]:
#             val_1 = stack.pop()
#             val_2 = stack.pop()
#             res = f"({val_2}{item}{val_1})"
#             stack.push(res)
#         else:
#             stack.push(item)
#     return stack.to_string()

# print(rpn( ["2", "1", "+", "3", "*"]))



            