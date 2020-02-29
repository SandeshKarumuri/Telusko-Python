f = open("Data", 'r')

f1 = open('abc.txt','w')
for data in f:
    f1.write(data)