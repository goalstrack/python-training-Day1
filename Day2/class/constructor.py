class Employee:
    empno=0
    salary=0
    grade=''    
    #parameterized
    def __init__(self,a,b,c):
        self.empno=a
        self.salary=b
        self.grade=c
        print('const called')
    def show(self):
        print(self.empno," ",self.salary," ",self.grade)
    def __del__(self):
        print('Bye!!!')

emp=Employee(101,34000,'A')
emp.show()
emp1=Employee(103, 13029, 'B')
emp1.show()
