def Hi():
    global a
    print(a)#this will take global reference
    a='Hello'#it wil confuse hence will give error so we can use global keyword for prevois one
    print(a)
    
a='My Python'
Hi()