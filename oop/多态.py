class Person(object):
    def __init__(self, name, gender):
      self.name = name
      self.gender = gender
    def whoAmI(self):
        return 'I am a person, my name is %s' %self.name


class Student(Person):
    def __init__(self, name, gender,score):
       super(Student, self).__init__(name, gender) 
       self.score = score
    def whoAmI(self):
        return 'I am a Student, my name is %s' %self.name

class Teacher(Person):
    def __init__(self, name, gender,course):
       super(Teacher, self).__init__(name, gender) 
       self.course = course 
    def whoAmI(self):
        return 'I am a Teacher, my name is %s' %self.name

def who_am_i(x):
    print(x.whoAmI())

p=Person('Tim','Male')
s=Student('Bob','Female',88)
t=Teacher('Alice', 'Female', 'English')

who_am_i(p)
who_am_i(s)
who_am_i(t)



   