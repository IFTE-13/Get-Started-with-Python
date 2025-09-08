# Concatenation ("+") Operator
T1 = (10, 20, 30)
T2 = ("Ten", "Twenty", "Thirty")
T3 = T1+ T2
print(T3)

# List Comprehension
# new_list = [expression for item in iterable]
T4 = [item for subtuple in [T1, T2] for item in subtuple]
print(T4)

# extend() Function
T5 = (1, 2, 3)
T6 = (4, 5, 6)
L5 = list(T5)
L6 = list(T6)
L5.extend(L6)
T5 = tuple(L5)
print(T5)

# sum() Function
# result_tuple = sum((tuple1, tuple2), ())
T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
T3 = sum((T1, T2), ())
print(T3)

# for loop
T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
for t in T2:
    T1 += (t, )
print(T1)