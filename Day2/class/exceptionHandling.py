try:
    a=int(input('Enter a number'))
    b=int(input('Enter a number '))
    c=a/b
    print(c)
except ZeroDivisionError:
    print('check 2nd num')
    