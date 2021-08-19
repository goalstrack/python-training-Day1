import pandas as pd
df=pd.read_csv('StudentDataForPivot.csv')

print(pd.pivot_table(df,index=['Name','Subject'],values='Score',aggfunc='sum'))
