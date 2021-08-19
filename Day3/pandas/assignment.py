import pandas as pd
empdf={'empno':[801,802,803,804,805],
       'name':['ravi','kiran','pooja','rakesh','disha'],
       'basic':[20000,14900,34000,12900,11890]}
empdf1=pd.DataFrame(empdf)
empdf1['hra']=(empdf1['basic'])*(0.12)
empdf1['total']=empdf1['hra']+empdf1['basic']
print(empdf1)