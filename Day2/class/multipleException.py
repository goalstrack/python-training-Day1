import sys
try:
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    c=a/b
    print(c)
except IndexError:
    print("No values provided: index error")
except ValueError:
    print("Incorrect values provided")
except ZeroDivisionError:
    print("2nd number should be non zero")
    