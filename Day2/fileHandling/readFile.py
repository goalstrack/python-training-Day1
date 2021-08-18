
fn=input('Enter File Name. ')

f=open(fn,'r')

st=f.read(2000)

print(st)

f.close()