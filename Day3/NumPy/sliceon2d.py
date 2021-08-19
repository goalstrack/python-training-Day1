import numpy as np

x=np.array([[12,34,65],
           [32,11,77],
           [78,44,23],
           [3,6,99]])
#any row 2nd column
print(x[...,2])
#2nd row any value
print(x[2,...])
#any row col 1 onwards values
print(x[...,1:])

#conditional slicing
print(x[x>35])