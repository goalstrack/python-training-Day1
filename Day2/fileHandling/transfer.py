import datetime

d=datetime.datetime.now()
d1=d.date()
print(d1)
if d1.day==18:
    fn=input('Enter File Name. ')
    tf=input('Enter destination file name')
    f=open(fn,'r')
    st=f.read(2000)
    df=open(tf,'w')
    df.write(st)
    f.close()
    df.close()
else:
    print('You cant transfer now ')