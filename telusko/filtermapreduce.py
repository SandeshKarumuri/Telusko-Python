from functools import reduce
# def is_even(n):
#     return n%2==0
# def update(n):
#     return n*2
# def add_all(a,b):
#     return a+b
nums= [3,4,5,6,58,5,4,9,2,8,9,106]
#evens= list(filter(is_even,nums))
evens = list(filter(lambda n:n%2==0,nums))
print(evens)
# doubles = list(map(update,evens))
doubles = list(map(lambda n:n*2,evens))
print(doubles)
# sum = reduce(add_all,doubles)
sum = reduce(lambda a,b : a+b,doubles)
print(sum)