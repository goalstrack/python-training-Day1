import pymysql

conn1=pymysql.Connect(host='localhost',user='root',password='Cloud@123$',db='fis')
#step 2
a=int(input('Enter EmpNo ==> '))
cur=conn1.cursor()
sql="select * from employee where empno=%d"%(a)
try:
    cur.execute(sql)
    data=cur.fetchone()
    if data != None:
        print('record present')
    else:
        b=input('Enter EmpName ==> ')
        c=input('Enter EmpCity ==> ')
        d=int(input('Enter EmpSalary ==> '))
        sql1="insert into employee values(%d,'%s','%s',%d)"%(a,b,c,d)
        cur.execute(sql1)
        print('record saved')
        conn1.commit()
except Exception as ex:
    print(ex)
        

conn1.close()