import numpy as np
x=np.array([[12,34,65],
           [32,11,77],
           [78,44,23],
           [3,6,8]])
#min
print(np.amin(x))
#min col wise
print(np.amin(x,0))
#min row wise
print(np.amin(x,1))
#max
print(np.amax(x))
#max col wise
print(np.amax(x,0))
#max row wise
print(np.amax(x,1))