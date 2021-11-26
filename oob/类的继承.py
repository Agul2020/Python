class Person(object):
   def __init__(self, name, gender):
      self.name = name
      self.gender = gender

class Student(Person):
   def __init__(self, name, gender,score):
       super(Student, self).__init__(name, gender) 
       self.score = score

s1=Student('张三','Female',89)
print(s1.name)

   