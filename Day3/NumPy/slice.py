import numpy as np

x=np.array([32,1,5,4,3,1,6,9])

#start 2 gap of 2 till 6 index
y=slice(1,8,2)

print(x[y])
#without slice function
y1=x[2:7:2]
print(y1)