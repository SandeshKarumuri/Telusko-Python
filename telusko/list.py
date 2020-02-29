Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2+3
5
>>> 5/2
2.5
>>> 5.5/2.5
2.2
>>> 5//2
2
>>> 8**2
64
>>> 10/2
5.0
>>> 10/3
3.3333333333333335
>>> 10%3
1
>>> x=2
>>> x++
SyntaxError: invalid syntax
>>> ++x
2
>>> x
2
>>> 19+x
21
>>>  nums=[90,67,87]
SyntaxError: unexpected indent
>>> nums=[90,67,87]
>>> names=['Sandesh','Karumuri']
>>> mil=[nums,names]
>>> mil
[[90, 67, 87], ['Sandesh', 'Karumuri']]
>>> nums.append(40)
>>> mil
[[90, 67, 87, 40], ['Sandesh', 'Karumuri']]
>>> nums.insert(2,80)
>>> mil
[[90, 67, 80, 87, 40], ['Sandesh', 'Karumuri']]
>>> nums.remove(67)
>>> nums
[90, 80, 87, 40]
>>> nums.pop(1)
80
>>> nums
[90, 87, 40]
>>> min(nums)
40
>>> max(nums)
90
>>> sum(nums)
217
>>> nums.sort()
>>> nums
[40, 87, 90]
>>> 
