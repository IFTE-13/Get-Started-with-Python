# Write a function called right_justify that takes a single string s as a parameter and prints the string right-aligned so that its last character appears in column 70 of the display.

def right_justify(s):
    """
    Prints the string s right-justified so that its last character
    is in column 70.
    """
    # Calculate number of spaces needed
    num_spaces = 70 - len(s)
    print(" " * num_spaces + s)

# Example usage
right_justify("allen")