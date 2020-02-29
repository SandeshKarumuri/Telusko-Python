
def Addition(a,b):
    print(a+b)
def Sub(a,b):
    return(a-b)
def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
result1,result2=add_sub(10,5)
print(result1,result2)
c=Sub(7,4)
print(c)
Addition(3,4)


def update(x):
    x=8
    print("x ",x)
a=10
update(a) #original value doesnt change
print("a ",a)

def updatelist(lst):
    print(id(lst))
    lst[1]=9
    print(id(lst))
    print("lst ",lst)

lst=[29,38,39]
print(id(lst))
updatelist(lst) #original value changes
print("lst ",lst)

#Types of Arguments default,keyword,position, variable length
def sum(a,*b):   #variable length is used for dynamic number of arguments
    c=a
    for i in b: # b is treated as a tuple
        c=c+i
    print(c)
sum(5,6,7)

def person(name,**data): #variable length ** is used for keyword arguments
    print("name ",name)
    for i,j in data.items():    #data is trated as a value-pair
        print(i,j)
person("Sandesh",age=20,city="Mogaltur",mob=9182338226)