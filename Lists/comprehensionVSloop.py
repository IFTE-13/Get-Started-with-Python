# List comprehensions are like shortcuts for creating lists in Python. They let you generate a new list by applying an operation to each item in an existing list.

# For loop, on the other hand, is a control flow statement used to iterate over elements of an iterable one by one, executing a block of code for each element.

# List comprehensions are often preferred for simpler operations, while for loops offer more flexibility for complex tasks.

# For Loop
chars=[]
for ch in 'TutorialsPoint':
   if ch not in 'aeiou':
      chars.append(ch)
print (chars)

# Coprehension
# listObj = [x for x in iterable]
chars = [ char for char in 'TutorialsPoint' if char not in 'aeiou']
print (chars)

# Result -> ['T', 't', 'r', 'l', 's', 'P', 'n', 't']

# Advantages of List Comprehension
# Conciseness − List comprehensions are more concise and readable compared to traditional for loops, allowing you to create lists with less code.

# Efficiency − List comprehensions are generally faster and more efficient than for loops because they are optimized internally by Python's interpreter.

# Clarity − List comprehensions result in clearer and more expressive code, making it easier to understand the purpose and logic of the operation being performed.

# Reduced Chance of Errors − Since list comprehensions are more compact, there is less chance of errors compared to traditional for loops, reducing the likelihood of bugs in your code.