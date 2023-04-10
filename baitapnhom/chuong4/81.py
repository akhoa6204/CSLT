import math
def nhap():
    a=float(input('canh goc vuong 1='))
    b=float(input('canh goc vuong 2='))
    return a,b
def tinh(a,b):
    c=math.sqrt(a*a+b*b)
    return c 
def inkq(c):
    print('chieu dai canh huyen=',c,sep='')

a,b=nhap()
c=tinh(a,b)
inkq(c)
    