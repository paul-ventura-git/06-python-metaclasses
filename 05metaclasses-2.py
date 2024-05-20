class MyMeta(type): # MyMeta can now create classes on the fly

    def __call__(cls, *args, **kwargs):
        print(f'{cls.__name__} is called'
              f'with args={args}, kwargs={kwargs}')
        print('metaclass calls __new__')
        obj = cls.__new__(cls, *args, **kwargs)

        if isinstance(obj, cls):
            print('metaclass calls __init__')
            cls.__init__(obj, *args, **kwargs)

        return obj

class Parent(metaclass=MyMeta):

    def __new__(cls, name, age):
        print('new is called')
        return super().__new__(cls)

    def __init__(self, name, age):
        print('init is called')
        self.name = name
        self.age = age

parent = Parent('John', 35)
# Parent is called with args=('John', 35), kwargs={}
# metaclass calls __new__
# new is called
# metaclass calls __init__
# init is called

print(type(parent))
# Parent

print(str(parent))
# '<__main__.Parent object at 0x103d540a0>'