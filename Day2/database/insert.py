import pymysql

conn1=pymysql.Connect(host='localhost',user='root',password='Cloud@123$',db='fis')
#step 2
cur=conn1.cursor()
sql="insert into employee values(109,'Bhakti','Pune',54000)"
try:
    cur.execute(sql)
    print('record saved')
    conn1.commit()
except Exception as ex:
    print(ex)
conn1.close()