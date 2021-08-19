import pandas as pd
import matplotlib.pyplot as plt
emp={'empno':[801,802,803,804,805],
       'name':['ravi','kiran','pooja','rakesh','disha'],
       'salary':[20000,14900,34000,12900,11890]}
empdf=pd.DataFrame(emp)
empdf['tax']=empdf['salary']*0.30
plt.bar(empdf['name'],empdf['tax'],color='blue')
plt.legend()
plt.title('Name-tax on salary')
plt.xlabel('Employee Name')
plt.ylabel('Tax on salary')

plt.show()