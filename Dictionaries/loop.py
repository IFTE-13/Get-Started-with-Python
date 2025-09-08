# For loop
student = {"name": "Alice", "age": 21, "major": "Computer Science"}
for key in student:
   print(key, student[key])
   
for key, value in student.items():
   print(key, value)
   
# dict.items() Method
for key in student.keys():
   print(key)