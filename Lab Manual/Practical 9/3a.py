class A:
    def b(self):
        print("c")
class D(A):
    def e(self):
        print("f")
x=D()
x.b()
x.e()
