import pandas as pd
df=pd.read_csv('Emp.csv')

df1=pd.read_csv('EmpGrade.csv')
#merge csv on the basis of common property
print(pd.merge(df,df1,on='EmpNo'))

