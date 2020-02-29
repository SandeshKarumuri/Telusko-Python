class Car:
    wheels=4    #static(class) variables
    def __init__(self):
        self.mil = 10   #instance variables are inside init
        self.com = "BENZ"

c1 = Car()
c2 = Car()
c1.mil=20
Car.wheels=5
print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)