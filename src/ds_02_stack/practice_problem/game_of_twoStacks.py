"""
Alexa has two stacks of non-negative integers, stack  and stack  where index  denotes the top of the stack. Alexa challenges Nick to play the following game:

In each move, Nick can remove one integer from the top of either stack  or stack .
Nick keeps a running sum of the integers he removes from the two stacks.
Nick is disqualified from the game if, at any point, his running sum becomes greater than some integer  given at the beginning of the game.
Nick's final score is the total number of integers he has removed from the two stacks.
Given , , and  for  games, find the maximum possible score Nick can achieve.
"""

def twoStacks(maxSum, a, b):
    # Write your code here
    move_sum = 0
    counter = 0
    a.reverse()
    b.reverse()
    last_item = []
    # while(move_sum<maxSum):
    #     if maxSum>move_sum+a[0]:
    #         move_sum+=a.pop(0)
    #         counter+=1
    #     elif maxSum>move_sum+b[0]:
    #         move_sum+=b.pop(0)
    #         counter+=1
    #     else:
    #         return counter
    # return counter
    while maxSum>move_sum:
        move_sum+=a[-1]
        last_item.append(a.pop())
        counter+=1
        
    move_sum-=last_item[-1]
    counter-=1
    
    while maxSum>move_sum:
        move_sum-=last_item[-1]
        move_sum+=b.pop()
        counter+=1
    
    move_sum-=last_item[-1]
    counter-=1
    
    return counter
        
    # while(maxSum>move_sum+a[0]):
    #         move_sum+=a.pop(0)
    #         counter+=1
    # while(maxSum>move_sum+b[0]):
    #         move_sum+=b.pop[0]
    #         counter+=1

print(twoStacks(62, [7 ,15, 12, 0, 5, 18, 17, 2, 10, 15, 4, 2, 9, 15, 13, 12, 16], [12, 16, 6, 8, 16, 15, 18, 3, 11, 0, 17, 7, 6, 11, 14, 13, 15, 6, 18, 6, 16, 12, 16, 11, 16, 11]))