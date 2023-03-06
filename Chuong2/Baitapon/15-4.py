import math
print('a,b,c là độ dài 3 cạnh tam giác')
a=int(input('a= '))
b=int(input('b= '))
c=int(input('c= '))
S=(a+b+c)/2
print('Dien tich= ',math.sqrt(S*(S-a)*(S-b)*(S-c)))