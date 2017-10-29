# 动态绑定实例属性与方法

class Student(object):
    pass


student = Student()
student.name = 'lee'
print(student.name)
print(hasattr(student, 'name'))


def bindMethod(self, method):
    from types import MethodType
    self.set_mathod = MethodType(method, self)


def set_mathod(self, age):
    self.age = age


bindMethod(student, set_mathod)
student.set_mathod(10)  # 指定实例绑定的函数,对其他实例无效
print(hasattr(student, 'age'))  # True

bindMethod(Student, set_mathod)  # 对于 class 绑定函数,影响所有实例
s1 = Student()
s1.set_mathod(10)
print(hasattr(s1, 'age'))  # True


# @property

class HighStudent(Student):
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    def __str__(self):
        return 'age is : ' + str(self.__age)

    def __repr__(self):
        return 'age repr : ' + str(self.__age)


histudent = HighStudent(10)
print(str(histudent.age))
print(str(histudent))
print(histudent)  # __repr__
