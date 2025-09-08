# Adding list items implies inserting new elements into an existing list.

# append() Method
#append() method is used to add a single element to the end of a list.
list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
list1.append('e')
print ("List after appending: ", list1)

# insert() Method
# The insert() method is used to add an element at a specified index (position) within a list, shifting existing elements to accommodate the new one.
list1 = ["Rohan", "Physics", 21, 69.75]
list1.insert(2, 'Chemistry')
print ("List after appending: ", list1)
list1.insert(-1, 'Pass')
print ("List after appending: ", list1)

# extend() Method
# The extend() method is used to add multiple elements from an iterable (such as another list) to the end of a list.
# Original list
list1 = [1, 2, 3]
# Another list to extend with
another_list = [4, 5, 6]

list1.extend(another_list)
print("Extended list:", list1)