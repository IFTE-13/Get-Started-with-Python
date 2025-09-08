# Python's decision making functionality is in its keywords − if..elif...else. The if keyword requires a boolean expression, followed by colon (:) symbol. 
# Here are some examples of decision-making constructs in Python:

# 1. If statement  
x = 10
if x > 5:
    print("x is greater than 5")
    
# 2. If-Else statement
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")
    
# 3. If-Elif-Else statement
z = 7   
if z > 10:
    print("z is greater than 10")
elif z > 5:
    print("z is greater than 5 but less than or equal to 10")
else:
    print("z is 5 or less")
    
# 4. Nested If statement
a = 15
if a > 10:
    if a < 20:
        print("a is between 10 and 20")
    else:
        print("a is 20 or greater")
else:
    print("a is 10 or less")

# 5. Ternary Conditional Operator
b = 8
result = "b is even" if b % 2 == 0 else "b is odd"
print(result)

# 6. Match-Case statement (Python 3.10+)
command = input()
match command:
    case "start":
        print("Starting the process")
    case "stop":
        print("Stopping the process")
    case "pause":
        print("Pausing the process")
    case _:
        print("Unknown command")
        
# These constructs help in making decisions and controlling the flow of execution in a Python program.
# You can run this code in a Python environment to see how each decision-making construct works.
