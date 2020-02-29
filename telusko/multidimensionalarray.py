from numpy import *
# 6 ways to create an array using numpy
arr= array([1,2,3],int)   #array()
print(arr.dtype)
print(arr)
print()
arr1=linspace(0,15,16)    #linspace(start,(include)stop,noofparts(default=50))
print(arr1)
print()
arr2=arange(1,15,2)       #arange(start,stop,step)
print(arr2)
print()
arr3=logspace(1,40,5)     #logspace()
print('%.2f' %arr3[3])
print()
arr4=zeros(5,int)
print(arr4)
print()
arr5=ones(5,int)
print(arr5)
print()
print()



arr1=array([[1,2,3,7,8,9],[4,5,6,10,11,12]]) #2-D Array
print(arr1.dtype)   #data type
print(arr1.ndim)    #Dimesion?
print(arr1.shape)   #no.of rows and columns?
print(arr1.size)    #no.of elements
print(arr1)
print()
arr2=arr1.flatten() #making multidimensional array as a 1d aray
print(arr2)
print()
arr3=arr2.reshape(3,4) #making 1d array to multidimensional reshape(rows,columns)
print(arr3)
print()
arr4=arr2.reshape(2,2,3)
print(arr4)

