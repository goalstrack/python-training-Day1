import pymysql

conn1=pymysql.Connect(host='localhost',user='root',password='Cloud@123$',db='fis')
#step 2
cur=conn1.cursor()
a=int(input('Enter Empno ==> '))
b=input('Enter EmpName ==> ')
c=input('Enter EmpCity ==> ')
d=int(input('Enter EmpSalary ==> '))
sql="insert into employee values(%d,'%s','%s',%d)"%(a,b,c,d)
try:
    cur.execute(sql)
    print('record saved')
    conn1.commit()
except Exception as ex:
    print(ex)
conn1.close()