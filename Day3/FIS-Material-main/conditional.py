import pandas as pd
df=pd.read_csv('salaries.csv')

#conditional data
dt=df[(df['salary']>90000)&
      (df['discipline']=='B')]

print(dt)

#Handling missing value
#replace by sum,max,min
print(df['service'])

#df['service'].fillna('0',inplace=True)
df['service'].fillna(df['service'].sum(),inplace=True)

print(df)