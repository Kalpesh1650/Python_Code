code_str = 'x = 5\ny = 10 \nprint("Sum = ",x+y)'
code = compile(code_str, 'sum.py', 'exec')

exec(code)

# The python exec() function is used for the dynamic execution of Python program which can
# either be a string or object code and it accepts large blocks of code

print('Below is the exec() function demo')
x = 8
exec('print(x==8)')
exec('print(x+4)')