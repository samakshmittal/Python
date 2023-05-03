class a:
    def b(self):
        print("c")
class d(a):
    def b(self):
        print("e")
class f(a):
    def b(self):
        print("g")
x=d()
x.b()
y=f()
y.b()
