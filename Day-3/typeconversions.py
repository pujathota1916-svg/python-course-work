Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(A)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    list(A)
NameError: name 'A' is not defined. Did you mean: 'a'?
tuple(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
bool(a)
True
bool(0)
False
b=10.5
int(b)
10
complex(b)
(10.5+0j)
str(b)
'10.5'
list(b)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
bool(b)
True
bool(0.0)
False
c=2+3j
int(c)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
list(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
str(c)
'(2+3j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
bool(c)
True
s='python'
a='43567'
b='345.678'
int(s)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'python'
int(a)
43567
int(b)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int(b)
ValueError: invalid literal for int() with base 10: '345.678'
float(s)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'python'
float(a)
43567.0
float(b)
345.678
>>> list(a)
['4', '3', '5', '6', '7']
>>> list(s)
['p', 'y', 't', 'h', 'o', 'n']
>>> list(b)
['3', '4', '5', '.', '6', '7', '8']
>>> tuple(s)
('p', 'y', 't', 'h', 'o', 'n')
>>> set(s)
{'t', 'p', 'y', 'n', 'h', 'o'}
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> int(a)
43567
>>> float(a)
43567.0
>>> float(b)
345.678
>>> bool(s)
True
>>> complex(s)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
>>> complex(a)
(43567+0j)
>>> complex(b)
(345.678+0j)
>>> l=[1,2,3,4,5]
>>> l
[1, 2, 3, 4, 5]
>>> int(l)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
>>> float(l)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
