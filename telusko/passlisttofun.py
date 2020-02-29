
def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if int(i)%2 is 0:
            even+=1
        else:
            odd+=1
    return even,odd



n=input("Enter elements for list:")
lst=n.split()
even, odd = count(lst)
print("Even : {} and Odd : {}".format(even,odd))
print("Even : %d and Odd : %d"%(even,odd))