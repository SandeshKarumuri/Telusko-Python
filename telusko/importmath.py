Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=sqrt(4)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    x=sqrt(4)
NameError: name 'sqrt' is not defined
>>> import math
>>> x=sqrt(4)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x=sqrt(4)
NameError: name 'sqrt' is not defined
>>> x=math.sqrt(4)
>>> x
2.0
>>> print(math.floor(2.5))
2
>>> print(math.ceil(2.5))
3
>>> print(math.ceil(2.6))
3
>>> print(math.floor(2.6))
2
>>> print(math.floor(2.1))
2
>>> print(math.ceil(2.1))
3
>>> print(math.pow(3,3))
27.0
>>> print(math.pi)
3.141592653589793
>>> print(math.e)
2.718281828459045
>>> import math as m
>>> m.sqrt(25)
5.0
>>> 
=============================== RESTART: Shell ===============================
>>> math.sqrt(25)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    math.sqrt(25)
NameError: name 'math' is not defined
>>> from math import sqrt,pow
>>> pow(4,5)
1024.0
>>> 
