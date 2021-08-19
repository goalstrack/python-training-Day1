import pandas as pd
df=pd.read_csv('salaries.csv')

#group on base of rank
# and sum of salary
dc=df.groupby(['rank'])

print(dc['salary'].sum())

