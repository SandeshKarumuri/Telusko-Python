#Constructor Inheritance
class A:
    def __init__(self):
        print("Constructor A")
    def feature1(self):
        print("Feature 1 Working")

    def feature2(self):
        print("Feature 2 Working")


class B(A):  # Single Inheritance

    def __init__(self): # If this constructor is not present , this class object calls A class constructor
        super().__init__() # this line calls super class constructor
        print("Constructor B")
    def feature3(self):
        print("Feature 3 Working")

    def feature4(self):
        print("Feature 4 Working")

a1=A()
b1=B()

#Method Resolution Order(MRO
class D:
    def __init__(self):
        print("Constructor D")
    def feature1(self):
        print("Feature 1 Working")

    def feature2(self):
        print("Feature 2 Working")


class E:

    def __init__(self):
        print("Constructor E")
    def feature3(self):
        print("Feature 3 Working")

    def feature4(self):
        print("Feature 4 Working")

class F(D,E):   # Multiple Inheritance maintain priority
    def __init__(self):
        super().__init__() #Starts from Left side of parenting
        print("Constructor F")
    def sup(self):
        super().feature3()

f1=F()
f1.sup()

