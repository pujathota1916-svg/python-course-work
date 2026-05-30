Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=12
>>> b=12.5
>>> c="python"
>>> print(a,b,c)
12 12.5 python
>>> print("a=",a,"b=",b,"c=",c)
a= 12 b= 12.5 c= python
>>> print("a=",a,"b=",b,"c=",c,sep='')
a=12b=12.5c=python
>>> print("a=",a,"b=",b,"c=",c,sep='\n')
a=
12
b=
12.5
c=
python
>>> print("a=",a,"b=",b,"c=",c,sep='',end='@@@')
a=12b=12.5c=python@@@
>>> print(f'a={a} b={b} c={c}')
a=12 b=12.5 c=python
>>> print('a=%d b=%.2f c%s' %(a,b,c))
a=12 b=12.50 cpython
>>> print('a={} b={} c={}'.format(a,b,c))
a=12 b=12.5 c=python
>>> print('a={2} b={0} c={1}'.format(a,b,c))
a=python b=12 c=12.5
>>> 
