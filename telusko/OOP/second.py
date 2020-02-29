class Computer:
    def __init__(self):
        self.name="Sandesh"
        self.age=20
    def update(self):
        self.age=21
    def compareage(self,other):
        if self.age==other.age:
            print("True")
        else:
            print("False")

c1 = Computer()
c2 = Computer()
c1.name="Pavan"
c1.age=19
print(c1.age)
c1.update()
print(c1.name)
print(c1.age)
print(c2.name)
# if c1.age == c2.age:
#     print("They are Same")
c1.compareage(c2)