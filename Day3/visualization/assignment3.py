import matplotlib.pyplot as plt
import pymysql

conn1=pymysql.Connect(host='localhost',user='root',password='Cloud@123$',db='fis')

cur=conn1.cursor()
sql="select ename,salary from employee"
try:
    cur.execute(sql)
    data=cur.fetchall()
    name=[]
    salary=[]
    for res in data:
        name.append(res[0])
        salary.append(res[1])
    plt.bar(name,salary,color='red')
    plt.title('Employee and their salary')
    plt.xlabel('Employee Names')
    plt.ylabel('Salary')
    plt.show()    
except Exception as ex:
    print(ex)        

conn1.close()