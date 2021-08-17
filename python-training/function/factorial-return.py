
def fact(x):
    f=1
    while x>=1:
        f=f*x
        x=x-1
    return f

r=int(input('Enter number '))
d=fact(r)

print('Factorial  ',d)