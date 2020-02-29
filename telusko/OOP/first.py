class Computer:
    def __init__(self, cpu, ram):   #special
        # print("__init__ is a constructor in python")
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print("Config is ", self.cpu, self.ram)


comp1=Computer('i5',8)
comp2=Computer('i5',3)

comp1.config()
comp2.config()

