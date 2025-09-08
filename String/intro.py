# In Python, a string is an immutable sequence of Unicode characters. Each character has a unique numeric value as per the UNICODE standard. But, the sequence as a whole, doesn't have any numeric value even if all the characters are digits. To differentiate the string from numbers and other identifiers, the sequence of characters is included within single, double or triple quotes in its literal representation. Hence, 1234 is a number (integer) but '1234' is a string.

var1 = 'Hello World!'
var2 = "Python Programming"
print (var1)

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

# Updating Strings
var1 = 'Hello World!'
print ("Updated String :- ", var1[:6] + 'Python')

# Escape Sequences in Python (Backslash Notation)

# \a  -> Bell or alert (ASCII 0x07)
# Example: print("Hello\aWorld")  # produces a beep sound (if supported)

# \b  -> Backspace (ASCII 0x08)
# Example: print("Hello\bWorld")  # removes the last character before 'World'

# \cx -> Control-x
# Example: "\cA" means Control+A (used rarely in text processing)

# \C-x -> Control-x (same as above)
# Example: "\C-A" means Control+A

# \e  -> Escape (ASCII 0x1b)
# Example: "\e[31mHello\e[0m"  # used in ANSI escape codes for colors

# \f  -> Formfeed (ASCII 0x0c)
# Example: print("Hello\fWorld")  # moves to a new page in printers

# \M-\C-x -> Meta-Control-x
# Example: Used in old systems for extended key input

# \n  -> Newline (ASCII 0x0a)
# Example: print("Hello\nWorld")  # prints in two lines

# \nnn -> Octal notation (0–7 digits)
# Example: print("\101")  # 'A' (octal 101 = decimal 65)

# \r  -> Carriage return (ASCII 0x0d)
# Example: print("Hello\rWorld")  # 'World' overwrites 'Hello'

# \s  -> Space (ASCII 0x20)
# Example: "Hello\sWorld"  # same as "Hello World"

# \t  -> Horizontal Tab (ASCII 0x09)
# Example: print("Hello\tWorld")  # inserts a tab space

# \v  -> Vertical tab (ASCII 0x0b)
# Example: print("Hello\vWorld")  # prints with vertical spacing

# \x  -> Character x (literal x if nothing follows)
# Example: print("\x41")  # 'A' (hex 41 = decimal 65)

# \xnn -> Hexadecimal notation (00–FF)
# Example: print("\x48\x65\x6C\x6C\x6F")  # prints "Hello"
