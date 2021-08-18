class A:
    a=10
    msg='hello'
    def hello(self):
        print('hello parent!')
    def __str__(self):
        return self.msg
    
obj=A()
print(obj)