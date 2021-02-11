import sys

print(sys.getrecursionlimit())

sys.setrecursionlimit(2000)

print(sys.getrecursionlimit())

i = 1


def hello():
    global i
    print("Hello",i)
    i += 1
    hello()


hello()