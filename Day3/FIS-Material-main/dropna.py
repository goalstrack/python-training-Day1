import pandas as pd
df=pd.read_csv('salaries.csv')

#all null removed
dt=df.dropna()

print(dt)

