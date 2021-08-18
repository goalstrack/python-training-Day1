class MyException(Exception):#User defined Exception
    def showMessage(self):
        print('My Issue')

try:
    a=int(input('Enter a number '))
    if a<10:
        raise MyException()
    else:
        print('ok')
except MyException as ex:
    ex.showMessage()