def factorial(n): #without recursion
    f=1
    for i in range(1,n+1):
        f*=i
    return f
result = factorial(5)
print(result)

def fact(n):    #using recursion
    if n is 0:
        return 1
    return n*fact(n-1)

r=fact(5)
print(r)

