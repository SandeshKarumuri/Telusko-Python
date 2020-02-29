def fib(n):
    a,b=0,1
    if n<=0:
        print()
    elif n is 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)

fib(100)