import pandas as pd

data={'unemployment':
      [4.3,3.6,7.1,4.1,8.9,9.0,12.3]
      ,'MarketShare':
          [1200,1100,300,1300,800,910,1811]}

df=pd.DataFrame(data,columns=['unemployment',
                                  'MarketShare'])
print(df)
df.plot(x='unemployment',
        y='MarketShare',
        kind='scatter')