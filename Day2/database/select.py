import pymysql

conn1=pymysql.Connect(host='localhost',user='root',password='Cloud@123$',db='fis')
#step 2
cur=conn1.cursor()
sql="select * from employee"

cur.execute(sql)
data=cur.fetchall()
for res in data:
    print('Empno..',res[0])
    print('Name..',res[1])
    print('City..',res[2])
    print('Salary..',res[3])
conn1.close()