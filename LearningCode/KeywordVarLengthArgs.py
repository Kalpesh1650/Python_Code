# * in formal arguments used when we are receiving variable length arguments


def addition(a, *b):
    c = a

    for i in b:
        c = c + i
    print("Addition is = %d"%c)


addition(10, 5, 5, 66, 34, 56, 71, 23, 44)

# ** in formal arguments used when we are receiving data along with arguments


def person(name, **data):
    print(name)
    print(data)


person('Kalpesh', age='30', City='Pune', Mobile='9096506399')