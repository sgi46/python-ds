"""
List in python is an dynamic array that is the size of the array is not fixed initially.
There will be enough room is given in the runtime while initilizing the array.

List has following nature:
List is ordered, mutable and even have mixed data type item
Items are ordered (they maintain their position).
    
Lists are mutable (you can change elements).

Items can be of any type (even mixed types).

"""

#Different ways to initialize the list:
list_a = list()
print(type(list_a))
list_b = []
print(type(list_b))
list_c = ["one","two","three","four","five","six"]
print(type(list_c))

#OPERATIONS:
# Adding new element at the end of the list:
list_c.append(7) #-> ["one","two","three","four","five","six", 7]

# Insert new element at the specified index:
list_c.insert(0, "zero") #-> ["zero","one","two","three","four","five","six", 7]

#Removes an item from the list:
#By value:
list_c.remove("two") #-> ["zero","one","three","four","five","six", 7]

#By index:
list_c.pop(0)  #-> ["one","three","four","five","six", 7]

#Returns the index of first matching element in the list
list_c.index("three") #-> 1

#slicing the list[start_index, end_index]
list_c[0:2] #-> ["one","three"]
print(list_c[::-1]) #->[7, "six", "five", "four", "three", "one"], it reverses the list

#iterating over the list:
#approach 1: This will print each item from list one by one
print("FROM APPROACH 1")
for item in list_c:   
    print(item)

"""
approach 2: Suppose, if you don't want to print all the item from the list but only k items for some 
operation then this approach will be beneficial
Here k = 3
"""
print("FROM APPROACH 2")
for i in range(3): 
    print(list_c[i])


#modify an existing item in the list:
# print(list_c) #-> Before: ["one","three","four","five","six", 7]
# list_c[1] = "THREE"  # Replacing item at index 1 as "ONE"
# print(list_c) #-> After: ["one","THREE","four","five","six", 7]


# #Built-in methods for list you should know:
# list_c.sort() #-> sort the list in asceding order
# list_c.clear() #-> empty the list by clearing all items
# list_c.reverse() #-> Method to reverse the 1list
# list_c.copy() #-> copies the list
# len() #-> Returns the size of the list

'''
QUICK EXERCISE:

my_fruits = ['apple', 'banana', 'cherry']
# 1. Add 'mango'
# 2. Replace 'banana' with 'grape'
# 3. Remove 'apple'
# 4. Print the final list

'''