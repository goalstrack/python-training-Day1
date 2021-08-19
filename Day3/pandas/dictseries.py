import pandas as pd

st={'rollno':101,
    'name':'amit',
    'city':'pune',
    'marks':91}

s=pd.Series(st,index=['name','rollno','marks','city'])
print(s)

s1=pd.Series(54,index=['n','a','m','e'])
print(s1)