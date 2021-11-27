class Animal: 				# 定义父类
   def run(self):
      print ('调用父类方法')
class Cat (Animal): 			# 定义子类
   def run (self):
      print ('调用子类方法')
class Dog (Animal):			# 定义子类
   def run (self):
      print ('调用子类方法')

c = Dog()					# 子类实例
c. run ()					# 子类调用重写方法
