import pymysql

conn1=pymysql.Connect(host='localhost',user='root',password='Cloud@123$',db='fis')
#step 2
cur=conn1.cursor()
sql="update employee set salary=70000 where empno=102"
try:
    cur.execute(sql)
    print('record updated')
    conn1.commit()
except Exception as ex:
    print(ex)
conn1.close()