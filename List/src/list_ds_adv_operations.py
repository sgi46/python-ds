"""
"""
from functools import reduce
#LIST COMPREHENSION is a technique to minimize the number of lines by creating new list
#TRADITIONAL WAY
seq_tw = []
for i in range(5):
    seq_tw.append(i)

print(seq_tw) #-> [0, 1, 2, 3, 4]

#USING LIST COMPREHENSION
seq_lc = [i for i in range(5)]  #-> [0, 1, 2, 3, 4]
even_num = [i for i in range(20) if i%2==0]  #-> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


#ENUMERATE is useful when you want to get hold of index and value from the list
print("****ENUMERATE****")
for key, value in enumerate(even_num):
    print(key , value)

#SORTED
print("****SORTED****")
fruits = ["apple", "orange", "jack"]
print(sorted(fruits)) #-> sorting based on alphabets: ['apple', 'jack', 'orange']
print(sorted(fruits, key=len)) #-> sorting based on length of the word: ['jack', 'apple', 'orange']
print(sorted(fruits, reverse=True)) #-> reverse sort: ['orange', 'jack', 'apple']

#MAP : Apply a function to every item in a list.
print("****MAP****")
nums = [5, 10, 15]
new_map = list(map(lambda x: x+10, nums)) #-> [15, 20, 25]
print(new_map)

#"Reduce" a list into a single value, using a function that works on two items at a time. It needs additional import 
print("****REDUCE****")
new_reduce = reduce(lambda x, y: x*y*x, nums) #-> 937500
print(new_reduce)

#"Filter" helps to filter the item from the list
print("***FILTER***")
new_filter = list(filter(lambda x: x>=10, nums))
print(new_filter)
