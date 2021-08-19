import pandas as pd

d={'rollno':[101,102,103,104],
   'name':['bhakti','rashmi','veena','jigisha'],
   'marks':[32,12,56,34]}
df=pd.DataFrame(d,index=['rec1','rec2','rec3','rec4'])

print(df)
print(df['rollno'])
df['promote']=df['marks']+10
print(df)