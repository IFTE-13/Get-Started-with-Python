# Looping through tuple items refers to iterating over each element in a tuple sequentially.
   
# for loop
tup = (25, 12, 10, -21, 10, 100)
for num in tup:
   print (num, end = ' ')
   
# while loop
my_tup = (1, 2, 3, 4, 5)
index = 0

while index < len(my_tup):
   print(my_tup[index])
   index += 1
   
# indexing
tup = (25, 12, 10, -21, 10, 100)
indices = range(len(tup))
for i in indices:
   print ("tup[{}]: ".format(i), tup[i])