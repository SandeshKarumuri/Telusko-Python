f = open("Data", 'r')


print(f.readline(),end='') #Only 1 line
print(f.readline()) #2nd line here
print(f.read()) # Full data

f1= open('abc.txt','w')
f1.write("Something")
f1.write(" Nothing")

f2 = open('abc.txt','a')
f2.write(" Anything")

