
def add(a, b):
    print(__name__)
    print("a =",a,"b =",b," a+b = ",a+b)


def subtract(a, b):
    print(a-b)


def multiply(a, b):
    print(a*b)


def division(a, b):
    print(a/b)


def main():
    add(3, 5)
    subtract(3, 5)
    multiply(3, 5)
    division(3, 5)


if __name__ == "__main__":
    main()