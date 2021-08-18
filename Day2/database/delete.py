import pymysql

conn1=pymysql.Connect(host='localhost',user='root',password='Cloud@123$',db='fis')
#step 2
cur=conn1.cursor()
sql="delete from employee where empno=110"
try:
    cur.execute(sql)
    print('record deleted')
    conn1.commit()
except Exception as ex:
    print(ex)
conn1.close()