from functools import reduce

""" when function have only single return statement as expression then we can use lambda expression
 In Python , function is an object """
f = lambda a: a*a

print(f(5))

# Filter map reduce example. Filter will filter data from list, Map will perform operation on it based on some logic,
# reduce will perform some operation on mapped data like Sum, Average etc


nums = [2, 6, 5, 3, 4, 55, 7, 8, 4]

evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)

doubles = list(map(lambda n: n*2, evens))
print(doubles)

sumofDoubles = reduce(lambda a, b: a+b, doubles)
print(sumofDoubles)

