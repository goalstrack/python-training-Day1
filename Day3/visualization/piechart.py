import matplotlib.pyplot as plt

labels='up','mp','ap','delhi'
lit=[25,35,45,65]

col=['green','red','yellow','blue']
e=(0,0,0,0.1)
plt.pie(lit,explode=e,labels=labels)
plt.show()