Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=2
>>> y=3
>>> x+y
5
>>> x-y
-1
>>> x*y
6
>>> x?y
SyntaxError: invalid syntax
>>> x/y
0.6666666666666666
>>> x=8 #Assignment
>>> x
8
>>> x=+2
>>> x
2
>>> x+=2
>>> x
4
>>> x
4
>>> x-=2
>>> x
2
>>> x*=3
>>> x
6
>>> a,b=5,6
>>> a
5
>>> b
6
>>> a=5,b6
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a=5,b6
NameError: name 'b6' is not defined
>>> a=5,b=6
SyntaxError: can't assign to literal
>>> n=7
>>> n
7
>>> -n
-7
>>> n=-n
>>> n
-7
>>> a<b
True
>>> #Relational
>>> a>b
False
>>> a==b
False
>>> a=6
>>> a==b
True
>>> a<=b
True
>>> a>=b
True
>>> a!=b
False
>>> b=7
>>> a!=b
True
>>> #Logical
>>> a=5
>>> b=4
>>> a<8 and b<5
True
>>> a<8 and b<2
False
>>> a<8 or b<2
True
>>> x=True
>>> x
True
>>> not x
False
>>> x
True
>>> x= not x
>>> x
False
>>> 
