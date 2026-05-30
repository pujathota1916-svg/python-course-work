Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
9/2
4.5
a/b
2.0
9//2
4
a**2
400
6**3
216
a%b
0
17%4
1
17%3
2
a
20
b
10
a<b
False
10<b
False
a==b
False
a!=b
True
y = 5
y
5
y=y+5
y
10
y=y+10
y
20
y +=10
y
30
y+=10
\
y
40
y-=20
y
20
y*=4
y
80
y//=10
y
8
y%=2
y
0
y+=10
y
10
y/=2
y
5.0
y
5.0
a
20
b
10
a%10==0
True
a%20==0 and b%20==0 and a>b
False
a%20==0 or b%20==0 or a>b
True
a%20==0 or b%20==0 or a<b
True
a%22==0 or b%20==0 or a<b
False
not a>b
False
#str,list,tuple,set,dict
a = 'python programming'
a
'python programming'
'y' in a
True
'g' in a
True
'z' not in a
True
'r' not in a
False
l=['java','python','mysql','c++','c','html']
'mysql' in l
True
'javascript' in l
False
'c' in l
True
'c' in not l
SyntaxError: invalid syntax
'c
SyntaxError: incomplete input
'c++' in l
True
'c' not in l
False
t=('laptop','mobile','mouse','keyword')
t
('laptop', 'mobile', 'mouse', 'keyword')
'laptop' in t
True
'charger' in t
False
t ={1,2,3,4,56,7,78,23,56}
t
{1, 2, 3, 4, 7, 78, 23, 56}
4 in t
True
24 in t
False
50 in t
False
d={'egg':'oil'120,'sugar':40,'salt':30}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
d={'egg':8,'oil':120,'sugar':40,'salt':30}
'oil' in d
True
120 in d
False
'sugar' in d
True
'chilli in d
SyntaxError: incomplete input
'chilli' in d
False
l=[1,2,3,4,5]
m=[1,2,3,4,5]
l==m
True
n=m
n
[1, 2, 3, 4, 5]
n==m
True
l is m
False
n is m
True
id(1)
140735198851880
id(m)
1909549867008
id(n)
1909549867008
l is not m
True
n is not l
True
8 & 7
0
8
8
|
8 | 7
15
>>> 10^11
1
>>> ~12
-13
>>> ~15
-16
>>> ~19
-20
>>> ~70
-71
>>> 8>>2
2
>>> 15>>l
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    15>>l
TypeError: unsupported operand type(s) for >>: 'int' and 'list'
>>> 15>>1
7
>>> 15>>2
3
>>> 15>>3
1
>>> 15>>2
3
>>> 16<<1
32
>>> 4<<2
16
>>> a=12
>>> b=12.34
>>> c='python'
>>> print(a,b,c)
12 12.34 python
>>> print("a=",'b=',b,'c=',c)
a= b= 12.34 c= python
>>> print("a=",a,'b=',b,'c=',c,sep='',end='\n\n')
a=12b=12.34c=python

>>> print("a",a,'b=',b,'c=',c,sep='',end='@@@')
a12b=12.34c=python@@@
>>> a=12b=12.34c=python@@@@
SyntaxError: invalid decimal literal
>>> print(f'a=(a) b=(b) c=(c)')
a=(a) b=(b) c=(c)
