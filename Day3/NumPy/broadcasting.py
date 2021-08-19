import numpy as np
x=np.array([[12,34,65],
           [32,11,77],
           [78,44,23]])

y=np.array([[1,84,95],
           [36,19,7],
           [87,94,53]])
'''
print(x+y)
print(x-y)
print(x*y)
print(x/y)
'''
print(np.add(x,y))
print(np.subtract(x,y))
print(np.multiply(x,y))
print(np.divide(x,y))
print(np.mod(x,y))

print(np.transpose(x))
print(x.T)#transpose matrix

 