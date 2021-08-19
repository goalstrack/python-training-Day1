import pandas as pd

df=pd.read_csv('EmpData.csv')

c=df.groupby(df['City'])
cp=['red','green','blue']

c.sum().plot(kind='pie',y='Payment')