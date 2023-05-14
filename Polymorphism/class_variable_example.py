class MyClass:
    static_var = 0
 
    def __init__(self):
        MyClass.static_var += 1
        self.instance_var = MyClass.static_var
 
obj1 = MyClass()
print(obj1.instance_var)  # Output: 1
 
obj2 = MyClass()
print(obj2.instance_var)  # Output: 2
 
print(MyClass.static_var)  # Output: 2
