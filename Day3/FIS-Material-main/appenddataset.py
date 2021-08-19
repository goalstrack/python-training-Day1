import pandas as pd
df=pd.read_csv('salaries.csv')

df1=pd.read_csv('salaries1.csv')
df2=df.append(df1)

print(df2)

