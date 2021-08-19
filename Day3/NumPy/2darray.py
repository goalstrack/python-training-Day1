import numpy as np

#2-D Array
# 4x3 matrix
x=np.array([[12,34,65],
           [32,11,77],
           [78,44,23],
           [3,6,99]])

print(x)

x1=np.array([[12,34,65,12],
           [32,11,77,76],
           [78,44,23,89]])

print(x1)
#shape
print(x1.shape)
#change shape of array
x1.shape=(4,3)
print(x1)
#reshaping
y=x.reshape(6,2)
print(y)