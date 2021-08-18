import sys

a=int(sys.argv[1])
opr=sys.argv[2]
b=int(sys.argv[3])
#we can use sys.argv[2] instead of opr directly
if opr=='+':
    c=a+b
    print('sum.. ',c)
if opr=='-':
    c=a-b
    print('difference.. ',c)
if opr=='/':
    c=a/b
    print('division.. ',c)
if opr=='*':
    c=a*b
    print('multiplication.. ',c)
if opr=='%':
    c=a%b
    print('modulus.. ',c)

