class Employee:
    empno=0
    name=''
    def get(self,a,b):
        self.empno=a
        self.name=b
    def show(self):
        print(self.empno)
        print(self.name)

'''obj=Employee()
obj.empno=101
obj.name='bhakti'
print(obj.empno," ",obj.name)'''
obj=Employee()
obj.get(101,"bhakti")
obj.show()

obj1=Employee()
obj1.get(102,"Amit")
obj1.show()