import numpy as np

#1-D 0 to 9 array
#x=np.arange(10)

#1 D 3 to 29 array
x=np.arange(3,30)
print(x)

#1d 5 to 50 step of 5
x1=np.arange(5,51,5)
print(x1)
#x1.shape=(5,2)
y=x1.reshape(5,2)
print(y)