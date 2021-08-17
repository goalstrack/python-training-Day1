
def basicgen():
    yield 'a'
    yield 34
    yield 'c'
    
x=basicgen()
print(next(x))
print(next(x))
print(next(x))