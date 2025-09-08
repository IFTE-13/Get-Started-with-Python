# A list comprehension in Python is a concise way to create lists by applying an expression to each element of an iterable. These expressions can be arithmetic operations, function calls, conditional expressions etc.
# [expression for item in iterable]
# new_list = [expression for item in iterable if condition]

numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print (squared_numbers) # [1, 4, 9, 16, 25]

string = "hello world"
uppercase_letters = [char.upper() for char in string if char.isalpha()]
print(uppercase_letters)  # ['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']

# Comprehensions and Lambda
# lambda is a keyword used to create anonymous functions.
# An anonymous function is a function defined without a name. These functions are created using the lambda keyword followed by a comma-separated list of arguments, followed by a colon :, and then the expression to be evaluated.
original_list = [1, 2, 3, 4, 5]
doubled_list = [(lambda x: x * 2)(x) for x in original_list]
print(doubled_list)  

# Nested Loops in List Comprehension
list1=[1,2,3]
list2=[4,5,6]
CombLst=[(x,y) for x in list1 for y in list2] 
print (CombLst)

# Conditionals in List Comprehension
# Conditionals in Python refer to the use of statements like "if", "elif", and "else" to control the flow of a code based on certain conditions.
list1=[x for x in range(1,21) if x%2==0]
print (list1)