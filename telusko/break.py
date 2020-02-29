available=5
x=int(input("How many Candies do you want?:"))
i=1
while(i<=x):
    if(i>available):
        print("We are out of Candies!")
        break
    print("Candy")
    i+=1
print("Bye")
