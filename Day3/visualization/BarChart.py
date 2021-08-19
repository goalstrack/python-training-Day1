import matplotlib.pyplot as plt

sem=[1,3,5]
m1=[34,90,65]
sem2=[2,4,6]
m2=[43,76,51]

plt.bar(sem,m1,color='r')
plt.bar(sem2,m2,color='b')
plt.title('Bar Chart')
plt.show()