# two built-in functions to read the input from the keyboard.
input()       # reads input as a string
int(input())  # reads input and converts it to an integer

name = input("Enter your name : ") 
city = input("Enter your city : ") 

print ("Hello My name is", name)
print ("I am from", city)

# Note: input() function always returns a string. To convert the input to other data types, use the appropriate type conversion functions like int(), float(), etc. (e.g., int(input()) to convert input to an integer).

# --- IGNORE ---
# Note: In Python 2.x, there is a function called raw_input() that behaves like input() in Python 3.x. However, raw_input() is not available in Python 3.x.