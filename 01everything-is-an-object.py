# In Python, everything is an object.
# even though a class is a “template” that is used to create objects from it, 
# it is also an object itself.

class Person:
    pass

print("The id of the class: ")
print(id(Person))
# some memory location

class Child(Person):
    pass

print("The id of the subclass: ")
print(id(Child))
# some memory location

# Class objects are created, you can instantiate objects

child = Child()

print("The id of the object: ")
print(id(child))
# some memory location

