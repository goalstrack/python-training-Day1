
import pandas as pd
df=pd.read_csv('EmpData.csv')


dfg=df.groupby('City')
total=dfg['Payment'].sum()
total.plot(kind='bar')
