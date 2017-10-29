class Student(object):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

    def printScore(self):
        print(self.name + ' ' + self.pwd)


student = Student('lee', 'lee')
student.printScore()


class HighSchoolStudent(Student):
    # self  对象实例本身
    def __init__(self, name, pwd, age):
        Student.__init__(self, name=name, pwd=pwd)
        self.__age = age  # private

    def printScore(self):
        print(str(self.__age))


hiStudent = HighSchoolStudent('lee', 'lee', 10)
hiStudent.printScore()


class PrimarySchoolStudent(Student):
    pass


primaryStu = PrimarySchoolStudent('l', 'l')

print(isinstance(hiStudent, Student))
print(isinstance(primaryStu, Student))


def printStudentScore(student):
    student.printScore()


printStudentScore(hiStudent)


class Teacher(object):
    # 类属性:同名实例属性将覆盖类属性
    name = 'lee'

    def printScore(self):
        print('print student\'s value')
        pass


# 动态语言的多态
# 只需要看起来像鸭子那就是鸭子,而无需真正继承鸭子  => 有 printScore 函数
teacher = Teacher()
printStudentScore(teacher)
print(teacher.name)

print(hasattr(hiStudent, 'name'))
