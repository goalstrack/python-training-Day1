import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('EmpData.csv')
plt.plot(df['EmpCode'],df['Payment'],color='red',linestyle='--',
         linewidth=5)
plt.show()

