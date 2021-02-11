
a = int(input("Enter first number :"))
b = int(input("Enter second number : "))

try:
    print("Stream Opened")
    c = a/b
    print(c)


except ZeroDivisionError as zde:
    print("Caught Divide by Zero exception - ", zde)

except ValueError as ve:
    print("value error - ", ve)

except Exception as e:
    print("Something went wrong - ", e)

finally:
    print("Stream closed")
