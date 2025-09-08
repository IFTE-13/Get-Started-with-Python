# Python program control flow is regulated by various types of conditional statements, loops, and function calls.

# Loops:
# 1. For Loop
print("For Loop Example:")
for i in range(5):
    print(i)
    
# 2. While Loop
print("\nWhile Loop Example:")
count = 0
while count < 5:
    print(count)
    count += 1
    
# 3. Break Statement
print("\nBreak Statement Example:")
for i in range(10):
    if i == 5:
        break
    print(i)
    
# 4. Continue Statement
print("\nContinue Statement Example:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
    
# 5. Pass Statement
print("\nPass Statement Example:")
for i in range(5):
    if i == 3:
        pass  # Do nothing
    else:
        print(i)

# 6. Function Calls
print("\nFunction Call Example:")
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
# These constructs help in controlling the flow of execution in a Python program.

# 7. Nested Loops
print("\nNested Loop Example:")
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
        