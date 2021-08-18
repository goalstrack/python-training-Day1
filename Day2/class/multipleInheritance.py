class A:
    def hello(self):
        print('hello parent!')

class B:
    def sum(self,a,b):
        print('sum is.  ',(a+b))

#C is child of A and B
class C(A,B):
    def hi(self):
        print('multiple hii C')

obj=C()

obj.hello()
obj.hi()
obj.sum(21, 33)