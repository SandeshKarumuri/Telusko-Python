class A:
    def feature1(self):
        print("Feature 1 Working")

    def feature2(self):
        print("Feature 2 Working")


class B(A):  # Single Inheritance
    def feature3(self):
        print("Feature 3 Working")

    def feature4(self):
        print("Feature 4 Working")


class C(B): #Multi Level Inheritance
    def feature5(self):
        print("Feature 5 Working")


a1 = A()
a1.feature1()
a1.feature2()
b1 = B()
b1.feature3()
b1.feature4()
b1.feature1()
b1.feature2()
c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()

class D:
    def feature6(self):
        print("Feature 6 Working")

    def feature7(self):
        print("Feature 7 Working")


class E:
    def feature8(self):
        print("Feature 8 Working")

    def feature9(self):
        print("Feature 9 Working")


class F(D, E): #Multiple Inheritance
    def feature10(self):
        print("Feature 10 Working")


f1=F()
f1.feature6()
f1.feature7()
f1.feature8()
f1.feature9()
f1.feature10()

