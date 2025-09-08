# String concatenation in Python is the operation of joining two or more strings together.

#  Concatenation using '+' operator

str1="Hello"
str2="World"
print ("String 1:",str1)
print ("String 2:",str2)
str3=str1+str2
print("String 3:",str3)

# Concatenating String with space
blank=" "
str3=str1+blank+str2
print("String 3:",str3)

# Concatenation By Multiplying
newString = str1 * 3
print(newString)

# Concatenation using join() method
str1="Hello"
str2="World"
str3=' '.join([str1,str2])
print(str3)

