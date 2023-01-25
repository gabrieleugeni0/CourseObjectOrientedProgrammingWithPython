class NameMyMetaClass(type):
    def __new__(mcs, name, bases, namespace):
        print('__new__ da metaclass')

        if name == 'Person':
            raise Exception('Cannot use name Person')

        cls = super().__new__(mcs, name, bases, namespace)
        return cls

class Person1(metaclass=NameMyMetaClass):
    def __new__(cls, *args, **kwargs):
        print('__new__ da class Person')
        cls = super().__new__(cls)
        return cls

    def __init__(self, name, lastname):
        print('__init__ da class Person')
        self.name = name
        self.lastname = lastname

if __name__ == '__main__':
    print(type(Person1))
