# Looping through list items in Python refers to iterating over each element within a list. 

# For loop
# for item in list:
   # Code block to execute
lst = [25, 12, 10, -21, 10, 100]
for num in lst:
   print (num, end = ' ')
   
# While loop
# An index variable is used within a loop to keep track of the current position or index in a sequence, such as a list or array. It is generally initialized before the loop and updated within the loop to iterate over the sequence.
# while condition:
   # Code block to execute
my_list = [1, 2, 3, 4, 5]
index = 0

while index < len(my_list):
   print(my_list[index])
   index += 1
   
# with Index
# An index is a numeric value representing the position of an element within a sequence, such as a list, starting from 0 for the first element.
lst = [25, 12, 10, -21, 10, 100]
indices = range(len(lst))
for i in indices:
   print ("lst[{}]: ".format(i), lst[i])
   
# enumerate() Function
# for index, item in enumerate(iterable):
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
   print(index, fruit)