# The list methods enable you to manipulate lists easily and effectively, whether you are appending new items, removing existing ones, or even sorting and reversing the list.

# Printing All
print(dir([]))
print(help([].append))

# Add Elements
obj, seq, index = []
list.append(obj)        # Appends object obj to list.
list.extend(seq)        # Appends the contents of seq to list
list.insert(index, obj) # Inserts object obj into list at offset index

# Remove Elements
list.clear()            # Clears all the contents of the list.
list.pop(obj=list[-1])  # Removes and returns the last object or the object at the specified index from the list.
list.remove(obj)        # Removes the first occurrence of object obj from the list.

# Access Elements
list.index(obj)         # Returns the lowest index in list that obj appears
list.count(obj)         # Returns count of how many times obj occurs in the list.

# Copying and Ordering
list.copy()             # Returns a copy of the list object.
list.sort([obj])        # Sorts the objects in the list in place, using a comparison function if provided.
list.reverse()          # Reverses the order of objects in the list in place.