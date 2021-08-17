a='123'
b='45'
print(a+b)#concatenate string does not perform addition
print(int(a)+int(b))#converted to integer for addition

a=89
b=9
print(a+b)#performs integer addition
print(str(a)+str(b))#integer to string conversion

del a,b#deletes variable

#print(a,b) gives error now since variables are deleted
