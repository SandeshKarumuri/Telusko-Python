from numpy import *
arr1=array([1,2,3,4,5])
arr2=array([6,8,9,7,10])
arr3=arr1+arr2
print(arr3)
print()
print(sin(arr1))
print(cos(arr1))
print(log(arr1))
print(sqrt(arr1))
print(sum(arr1))
print(min(arr1))
print(max(arr1))
print(sort(arr2))
print(sort(concatenate([arr1,arr2])))
print()
arr4=arr1.copy()           #copying an array without a same address for both
#arr4=arr1              copying an array but both the array have same address so any array name can change the value for both
print(arr4)
