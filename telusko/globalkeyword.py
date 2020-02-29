a=10
def something():
    a=9
    #global a #is used for using global varible
    x=globals()['a']
    print("fun ",a)
    print("global a ", x)

something()
print("actual ",a)