from array import *
values=array('i',[2,3,4,-5,6])
for i in range(len(values)):
    print(values[i],end=" ")
print()


values.reverse()
for i in values:
    print(i,end=" ")
print()


newArr=array(values.typecode,(a**3 for a in values))
i=1
while i<len(newArr):
    print(newArr[i])
    i+=1

