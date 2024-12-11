class MyClass:
    class_variable = 0
    a = False

    def __init__(self, value):
        self.instance_variable = value

    @classmethod
    def class_method(cls, x):
        cls.class_variable += x
        return cls.class_variable

# Creating instances of the class
obj1 = MyClass(5)
obj2 = MyClass(10)

# Calling the class method
print(MyClass.class_method(3))
print(MyClass.class_method(7))

print(obj2.class_variable) 

obj2.class_method(3)

print(MyClass.class_method(3))
print(MyClass.class_method(7))
print(obj2.class_variable)