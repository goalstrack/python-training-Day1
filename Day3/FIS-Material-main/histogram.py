import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('EmpData.csv')

plt.hist(df['Payment'],bins=6)
plt.show()