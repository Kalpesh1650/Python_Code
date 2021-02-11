
def topten():

    n = 1

    while n <= 10:
        sq = n*n
        yield sq  # yield will return value but it won't terminate function control
        n += 1


values = topten()

for i in values:
    print(i)