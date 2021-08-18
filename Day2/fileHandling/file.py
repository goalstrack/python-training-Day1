
empno="101"
name="Amit"
city="Delhi"

obj=open("data.txt",'w')

obj.write(empno+'\n')
obj.write(name+'\n')
obj.write(city+'\n')

print('data saved')

obj.close()
