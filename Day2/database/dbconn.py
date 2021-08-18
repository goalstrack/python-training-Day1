import pymysql

conn=pymysql.Connect(host='localhost',user='root',password='Cloud@123$',db='fis')
#step 2
cur=conn.cursor()
sql='select version()'

cur.execute(sql)
data=cur.fetchone()
print(data)
conn.close()