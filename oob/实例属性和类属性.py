#定义含有实例属性（姓名name， 年龄age）和类属性（人数num）的Person人员类
class Person:
	num=1			#类属性
	def __init__(self, str,n):	#构造函数
		self.name = str	#实例属性
		self.age=n
	def SayHello(self): 		#成员函数
		print("Hello!")
	def PrintName(self): 		#成员函数
		print("姓名：", self.name,  "年龄：", self.age)
	def PrintNum(self): 		#成员函数
		print(Person.num)	#由于是类属性，所以不写self .num
#主程序
P1= Person("夏敏捷",42)
P2= Person("王琳",36)
P1.PrintName()
P2.PrintName()