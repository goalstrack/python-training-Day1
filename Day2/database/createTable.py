import pymysql

conn1=pymysql.Connect(host='localhost',user='root',password='Cloud@123$',db='fis')
#step 2
cur=conn1.cursor()
sql="create table test(empno int,month varchar(20))"
try:
    cur.execute(sql)
    print('Table created')
    conn1.commit()
except Exception as ex:
    print(ex)
conn1.close()