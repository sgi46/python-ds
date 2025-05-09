"""
For problem overview, refer: https://www.hackerrank.com/challenges/poisonous-plants/problem?isFullScreen=true
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def find_(ip_list):
    stack_index=[]
    print(f"iplist{ip_list}")
    print(f"stack_index:{stack_index}")
    for i in range(len(ip_list)-1):
        if ip_list[i]<ip_list[i+1]:
            stack_index.append(i+1)
        
    print(f"stack_index_after:{stack_index}")
    print(f"iplist_after{ip_list}")
    for index in sorted(stack_index, reverse=True):
        ip_list.pop(index)

    return ip_list
    
def poisonousPlants(p):
    # Write your code here
    day = 0
    initial_len = len(p)
    post_find=0
    while(initial_len!=post_find):
        print(initial_len)
        print(post_find)
        initial_len=len(p)
        find_(p)
        post_find=len(p)
        
        day+=1
        print("updated")
    return day-1
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    print(f"THE RESULT IS:{result}")
