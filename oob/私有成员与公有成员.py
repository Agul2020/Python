class Car:
    price = 100000 				 #定义类属性
    def __init__(self, c, w):
        self.color = c				 #定义公有属性color
        self. __weight= w			 #定义私有属性__weight
#主程序
car1 = Car("Red",10.5)
car2 = Car("Blue",11.8)
print(car1.color)
print(car1. _Car__weight)
print(car1. __weight)			 # AttributeError 
