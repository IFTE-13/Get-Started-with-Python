# String modification refers to the process of changing the characters of a string. If we talk about modifying a string in Python, what we are talking about is creating a new string that is a variation of the original one.

# String to list
string = "WORD"
print ("original string:", string)
list=list(string)
list.insert(3,"L")
print (list)

string=''.join(list)
print ("Modified string:", string)

# Array module
import array as arr
string = "WORD"
print ("original string:", string)
array = arr.array('u', string) # 'u' is the type code for Unicode characters which is deprecated since Python 3.3
array.insert(3, 'L')
print (array)
string = string.join(array)
print ("Modified string:", string)