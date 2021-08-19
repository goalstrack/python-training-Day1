import numpy as np
x=np.array([[12,34,65],
           [32,11,77],
           [78,44,23]])

y=np.array([[1,84,95],
           [36,19,7],
           [87,94,53]])

print(np.concatenate((x,y)))


print(np.concatenate((x,y),axis=1))