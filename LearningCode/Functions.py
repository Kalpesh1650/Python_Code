# Define our 3 functions

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

# prints - "Hello, John Doe, From My Function!, I wish you a great year!"
# my_function_with_args("John Doe", "a great year!")


def count(listofnumbers):

    even = 0
    odd = 0

    for i in listofnumbers:
        if i % 2 == 0:
            even += 1
            print("Even : ", i)
        else:
            odd += 1
            print("odd : ", i)

    return even, odd


listOfNumbers = [4,6,9,2,34,65,78,76,45,22,11]

even1, odd1 = count(listOfNumbers)

print(even1)
print(odd1)

