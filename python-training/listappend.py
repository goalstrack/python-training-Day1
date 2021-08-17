x=['a','b','c','p']

x.append('test')

print(x)

x.insert(3,'aju')
x.append('b')
x.append('b')

print(x)
print(x.count('b'))

r=['x','y','z']
#appended r into x
x.extend(r)
print(x)

print(x.index('b'))

print(x.pop())

print(x)
#order change
x.reverse()
print(x)