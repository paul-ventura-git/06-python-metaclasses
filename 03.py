# __new__ (implicitly) creates an instance before __init__ is called to initialize it.

class Parent:
    def __new__(cls, name, age):
        print('new is called')
        return super().__new__(cls) # Here it is the magic

    def __init__(self, name, age):
        print('init is called')
        self.name = name
        self.age = age

parent = Parent('John', 35)

print(isinstance(object, object))