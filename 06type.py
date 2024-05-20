# type(name, bases, attrs)
# name: name of the class
# bases: tuple of the parent class (for inheritance, can be empty)
# attrs: dictionary containing attributes names and values

print("########## First example ############")
MyShinyClass = type('MyShinyClass', (), {})
print(MyShinyClass)
print(MyShinyClass())
print(type(MyShinyClass))

print("########## Second example ############")
Foo = type('Foo', (), {'bar':True})
print(Foo)
print(Foo.bar)
f = Foo()
print(f)
print(f.bar)
print(type(Foo))

print("########## Third example ############")
def echo_bar(self):
  print(self.bar)

FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
print(hasattr(Foo, 'echo_bar'))
print(hasattr(FooChild, 'echo_bar'))

def echo_bar_more(self):
  print('yet another method')

FooChild.echo_bar_more = echo_bar_more
print(hasattr(FooChild, 'echo_bar_more'))