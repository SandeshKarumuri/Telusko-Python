from numpy import *
arr1=array([
            [1,2,3,4],
            [5,6,7,8]
            ])
#m=matrix(arr1) #directly converting array to matrix
m1=matrix('1,2,3;4,5,6;7,8,9')
m2=matrix('1,2,3;4,5,6;7,8,9')
print(m1)
print(diagonal(m1))
print(m1.min())
print(m1.max())
print()
m3=m1*m2;
print(m3)
m4=m1+m2;
print(m4)
m5=m1-m2;
print(m5)
