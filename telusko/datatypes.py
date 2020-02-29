Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=5
>>> type(num)
<class 'int'>
>>> num=2.5
>>> type(num)
<class 'float'>
>>> num=6+9j
>>> type(num)
<class 'complex'>
>>> a=5.2
>>> b=int(a)
>>> b
5
>>> type(b)
<class 'int'>
>>> k=(float)
>>> k
<class 'float'>
>>> k=float(b)
>>> k
5.0
>>> k=6
>>> c=complex(b,k)
>>> c
(5+6j)
>>> b<k
True
>>> k<6
False
>>> conda=b<k
>>> conda
True
>>> int(True)
1
>>> int(False)
0
>>> lst=[34,434,54,5,9]
>>> type(lst)
<class 'list'>
>>> s={43,56,78,98,9}
>>> type (s)
<class 'set'>
>>> t=(43,54,6,5,7,8,0)
>>> type(t)
<class 'tuple'>
>>> str="sandesh"
>>> type(str)
<class 'str'>
>>> range(0,10)
range(0, 10)
>>> list(range)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    list(range)
TypeError: 'type' object is not iterable
>>> list(range(0,20))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list(range(0,100,2))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> type(range(10))
<class 'range'>
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> d={"Sandesh":"Samsung","Vineeth":"Vivo","Raghavendra":"MI","Vamsi":"Honor"}
>>> d
{'Sandesh': 'Samsung', 'Vineeth': 'Vivo', 'Raghavendra': 'MI', 'Vamsi': 'Honor'}
>>> d.keys()
dict_keys(['Sandesh', 'Vineeth', 'Raghavendra', 'Vamsi'])
>>> d.values()
dict_values(['Samsung', 'Vivo', 'MI', 'Honor'])
>>> d['Sandesh']
'Samsung'
>>> d.get('Sandesh')
'Samsung'
>>> 
