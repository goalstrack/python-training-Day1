import pandas as pd
df=pd.read_csv('salaries.csv')

#head top 5 records bydefault and specific if mentioned
print(df.head(2))

#tail bottom 5 records
print(df.tail())

print(df.tail(3))

print(df.dtypes)

print(df)

print(df.shape)