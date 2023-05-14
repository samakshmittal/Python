class MyClass:
    def __init__(self, value):
        self.value = value
 
    def get_value(self):
        return self.value
 
# Create an instance of MyClass
obj = MyClass(10)
 
# Call the get_value method on the instance
print(obj.get_value())  # Output: 10
