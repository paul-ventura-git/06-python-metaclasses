# Specific methods in your class describe a Protocol 
# (a way of using its object),
# Methods are described by this 'Protocol'
class Parent:
    def __new__(cls, name, age):
        print('new is called')
        return super().__new__(cls)

    def __init__(self, name, age):
        print('init is called')
        self.name = name
        self.age = age

    def __call__(self): # One of these protocols are callable
        print('Parent here!')

parent = Parent('John', 35)
parent()
# Parent here!