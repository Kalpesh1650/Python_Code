###### -Tuple - #############
'''
Python Tuple is used to store the sequence of immutable Python objects.
The tuple is similar to lists since the value of the items stored in
the list can be changed, whereas the tuple is immutable, and the value
of the items stored in the tuple cannot be changed.
'''

T1 = (101, "Peter", 22)
T2 = ("Apple", "Banana", "Orange")
T3 = 10, 20, 30, 40, 50 # --  The tuple which is created without using parentheses is also known as tuple packing.

print(type(T1))
print(type(T2))
print(type(T3))

# - tuple with single element in it
tup2 = ("JavaTpoint",)
print(type(tup2))

tuple1 = (10, 20, 30, 40, 50, 60)
print(tuple1)

print('Tuple size =', tuple1.__sizeof__())
