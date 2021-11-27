class Person:
    num=0			#类属性
    def __init__(self, str,n,w):	#构造函数
        self.name = str		#对象实例属性（成员）
        self.age=n
        self.__weight= w		#定义私有属性__weight
        Person.num += 1
    def __outputWeight(self):	#定义私有方法outputWeight
        print("体重：",self.__weight)	#访问私有属性__weight
    def PrintName(self): 		#定义公有方法（成员函数）
        print("姓名：", self.name,  "年龄：", self.age, end=" ")
        self.__outputWeight( ) 	#调用私有方法outputWeight
    def PrintNum(self): 		#定义公有方法（成员函数）
        print(Person.num)		#由于是类属性，所以不写self.num
    @ staticmethod
    def getNum():		#定义静态方法getNum
         return Person.num

#主程序
P1= Person("夏敏捷",42,120)
P2= Person("张海",39,80)
#P1.outputWeight()			#错误'Person' object has no attribute 'outputWeight'
P1.PrintName()
P2.PrintName()
Person.PrintName(P2)
print("人数：",Person.getNum())
print("人数：",P1.getNum())
