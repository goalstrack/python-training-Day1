f=open('data1.txt','r')

st=f.read(150)

print(st)

pos=f.tell()

print('Position.. ',pos)
pos=f.seek(0,0)
st=f.read(10)
print(st)

f.close()