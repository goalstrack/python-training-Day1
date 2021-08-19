import pandas as pd
df=pd.read_csv('salaries.csv')

#sorting in ascending order
#print(df.sort_values('salary'))

#sorting in descending order
print(df.sort_values('salary',ascending=False))

