class A:
    def hello(self):
        print('hello parent!')

#B is child of A
class B(A):
    def sum(self,a,b):
        print('sum is.  ',(a+b))

#C is child of B
class C(B):
    def hi(self):
        print('multilevel hii')

obj=C()

obj.hello()
obj.hi()
obj.sum(21, 33)