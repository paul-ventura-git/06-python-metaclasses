class MyMeta(type):
    def __call__(self, *args, **kwargs):
        print(f'{self.__name__} is called'
              f' with args={args}, kwargs={kwarg}')

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
type(parent)
# NoneType