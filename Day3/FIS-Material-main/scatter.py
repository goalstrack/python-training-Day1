import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('EmpData.csv')

plt.scatter(df['Payment'],df['NoOfHours']
            ,marker='o')
plt.show()