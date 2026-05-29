Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
type(a)
<class 'int'>
t=75.45
type(t)
<class 'float'>
c=12+5j
type(c)
<class 'complex'>
s="shivpuja"
type(s)
<class 'str'>
>>> l=[1,2,3]
>>> id(l)
1612296869504
>>> l=['postl.png','reel.mp4']
>>> l
['postl.png', 'reel.mp4']
>>> l=[]
>>> l=list()
>>> type(1)
<class 'int'>
>>> t=(1,2,34,75,43)
>>> t
(1, 2, 34, 75, 43)
>>> type(t)
<class 'tuple'>
>>> s={1,2,3,4,6}
>>> type(s)
<class 'set'>
>>> s=set()
>>> s={45678,678,56789,897}
>>> a
10
>>> s
{897, 678, 56789, 45678}
>>> d={'name': 'abc': 'age': 100, 'course': 'PSF'}
SyntaxError: invalid syntax
>>> d={'name':'abc','age':100',course':'PSF'}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> d
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> d={'name':'abc','age':100,'couse':'PSF'}
>>> d
{'name': 'abc', 'age': 100, 'couse': 'PSF'}
>>> type(d)
<class 'dict'>
>>> status=True
>>> status=False
>>> type(status)
<class 'bool'>
>>> a=None
>>> type(a)
<class 'NoneType'>
