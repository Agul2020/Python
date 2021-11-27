class Person(object):
    count = 0
    @classmethod
    def how_many(cls):
        return cls.count
    def __init__(self,name):
        self.name = name
        Person.count = Person.count + 1

print(Person.how_many())
p1 = Person('Bob')
print(Person.how_many())
