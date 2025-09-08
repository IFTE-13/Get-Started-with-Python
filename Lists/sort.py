# Sorting a list in Python is a way to arrange the elements of the list in either ascending or descending order based on a defined criterion, such as numerical or lexicographical order.

# sort() Method
# list_name.sort(key=None, reverse=False)
# list_name is the name of the list to be sorted.
# key (optional) is a function that defines the sorting criterion. If provided, it is applied to each element of the list for sorting. Default is None.
# reverse (optional) is a boolean value. If True, the list will be sorted in descending order. If False (default), the list will be sorted in ascending order.
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# Sorting in descending order
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc) 

# Lexicographical Order
list1 = ['physics', 'Biology', 'chemistry', 'maths']
print ("list before sort:", list1)
list1.sort()
print ("list after sort : ", list1)

# Numerical Order
list2 = [10,16, 9, 24, 5]
print ("list before sort", list2)
list2.sort()
print ("list after sort : ", list2)

# Callback Function
# We can sort list items with a callback function by using the sorted() function or sort() function. Both of these functions allows us to specify a custom sorting criterion using the "key" parameter, which accepts a callback function. This callback function defines how the elements should be compared and sorted.

# str.lower() as key Parameter
list1 = ['Physics', 'biology', 'Biomechanics', 'psychology']
print ("list before sort", list1)
list1.sort(key=str.lower)
print ("list after sort : ", list1)

# user-defined Function as key Parameter
def myfunction(x):
   return x%10
list1 = [17, 23, 46, 51, 90]
print ("list before sort", list1)
list1.sort(key=myfunction)
print ("list after sort : ", list1)