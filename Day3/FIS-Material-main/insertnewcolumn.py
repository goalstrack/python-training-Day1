import pandas as pd
df=pd.read_csv('salaries.csv')

#insert new column
df.insert(6,'test',df['service']+20)

print(df)

