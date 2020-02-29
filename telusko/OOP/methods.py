# 2 types of methods: Accessor and Mutator
class Student:
    school = "Sandesh"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):  # Accessor or Getter
        return self.m1

    def set_m1(self, val):  # Mutator or Setter
        self.m1 = val

    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is Student class")


s1 = Student(12, 45, 89)
s2 = Student(45, 85, 65)
print(s1.avg())
print(s2.avg())
print(Student.getschool())
Student.info()
