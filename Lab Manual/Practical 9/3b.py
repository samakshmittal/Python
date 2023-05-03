class a:
    def b(self):
        print("c")
class d:
    def e(self):
        print("f")
class g(a, d):
    def h(self):
        print("i")

x=g()
x.b()
x.e()
x.h()
