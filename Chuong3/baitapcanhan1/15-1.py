import math
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a>0 and b>0 and c>0 and (a+b)>c and (a+c)>b and (b+c)>a:
   p=(a+b+c)/2
   print('Dien tich=',round(math.sqrt(p*(p-a)*(p-b)*(p-c)),3),sep='')
else:
    print('Khong hop le')