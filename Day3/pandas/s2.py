import pandas as pd

#s=pd.Series(['p','x','r','k','a']) default index from o
s=pd.Series(['p','x','r','k','a'],
            index=[121,190,321,87,99])

print(s)

s2=pd.Series([3,6,2,1,8,10],
             index=['w','t','e','o','p','f'])
print(s2)

#index for search
print(s2['f'])