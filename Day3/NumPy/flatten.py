import numpy as np
x=np.array([[12,34,65],
           [32,11,77],
           [78,44,23]])

print(x.flatten())#converts to 1d array

print(x.flatten(order='F'))#traverse column wise