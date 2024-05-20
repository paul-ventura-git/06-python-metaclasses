# the interpreter goes through the class definition, 
# and once the class code block is finished, the class object is created.

#type functions
class Person:
    pass

class Child(Person):
    pass

child = Child()

print(type(child)) # it gives the name of its "creator"
# Child

print(type(Child))
# type

# "An object is an instance of a class, and a class is an instance of a type."