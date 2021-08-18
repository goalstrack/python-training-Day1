class A:
    def hello(self):
        print('hello parent!')

#B is child of A
class B(A):
    def sum(self,a,b):
        print('sum is.  ',(a+b))

obj=B()
obj.sum(21, 33)
obj.hello()