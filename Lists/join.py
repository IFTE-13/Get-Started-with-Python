# Joining lists in Python refers to combining the elements of multiple lists into a single list. This can be achieved using various methods, such as concatenation, list comprehension, or using built-in functions like extend() or + operator.

# Concatenation Operator
# The concatenation operator, denoted by +, is used to join two sequences, such as strings, lists, or tuples, into a single sequence. When applied to lists, the concatenation operator joins the elements of the two (or more) lists to create a new list containing all the elements from both lists.
# Two lists to be joined
L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']
# Joining the lists
joined_list = L1 + L2

# Printing the joined list
print("Joined List:", joined_list)

# List Comprehension
# new_list = [expression for item in iterable]
# This creates a new list where expression is evaluated for each item in the iterable.
# Two lists to be joined
L1 = [36, 24, 3]
L2 = [84, 5, 81]
# Joining the lists using list comprehension
joined_list = [item for sublist in [L1, L2] for item in sublist]
# Printing the joined list
print("Joined List:", joined_list)

# append() Function
# extend() Function
