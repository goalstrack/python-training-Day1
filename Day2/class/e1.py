class Employee1:
    empno=0
    salary=0
    grade=''
    def get(self,a,b):
        self.empno=a
        self.salary=b
    def check(self):
        if self.salary>30000:
            self.grade='A'
        else:
            self.grade='B'
    def show(self):
        self.check()
        print(self.empno)
        print(self.grade)

obj=Employee1()
obj.get(103,31000)
obj.show()
print(hasattr(obj, 'empno'))#show if attribute present or not
print(hasattr(obj, 'name'))

print(getattr(obj, 'salary'))
setattr(obj, 'salary', 45000)

print(getattr(obj, 'salary'))

delattr(obj, 'salary')
print(hasattr(obj, 'salary'))