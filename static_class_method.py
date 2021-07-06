
class Student(object):
    count = 0
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.count = self.count + 1
    def msg(self):
        print("count {} - {} got {} marks".format(self.count, self.name, self.marks))

    @classmethod
    def objectCount(cls):
        return cls.count

s1 = Student("venkat", "899")
s1.msg()
s2 = Student("Rajesh", "809")
s2.msg()
s3 = Student("Vamsi", "909")
s3.msg()

print(Student.objectCount())