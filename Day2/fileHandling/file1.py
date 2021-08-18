
empno=int(input('Enter EMployye no.. '))
name=input('Enter Name. ')
city=input('Enter City. ')

fn=input('Enter File Name. ')
obj=open(fn,'a')

obj.write(str(empno)+'\n')
obj.write(name+'\n')
obj.write(city+'\n')

print('data saved')

obj.close()
