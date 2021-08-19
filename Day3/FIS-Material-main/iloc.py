import pandas as pd
df=pd.read_csv('salaries.csv')

print(df)

# row 0 to 1  & col 0 to 2
print(df.iloc[0:2,0:3])

