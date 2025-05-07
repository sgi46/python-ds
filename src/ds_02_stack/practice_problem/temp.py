"""
Given a list of daily temperatures, 
return a list where each index tells you how many days to wait until a warmer temperature.
Input:  [73,74,75,71,69,72,76,73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
"""
from src.ds_02_stack.build_stack import Stack

def find_warm(temps):

    stack_wait = []
    answer = [0]*len(temps)

    for i, temp in enumerate(temps):
        while stack_wait and temp>temps[stack_wait[-1]]:
            prev_index = stack_wait.pop()
            answer[prev_index] = i - prev_index
        stack_wait.append(i)

    return answer


print(find_warm([73, 74, 75, 71, 69, 72, 76, 73]))