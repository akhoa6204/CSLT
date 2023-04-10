import math 
def nhap():
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    return a,b,c

def giaipt(a,b,c):
    s=b*b-4*a*c
    if s<0:
        print('Phuong trinh vo nghiem')
        return None
    elif s==0:
        x1=x2=-b/(2*a)    
    elif s>0:
        x1=(-b+math.sqrt(s))/(2*a)
        x2=(-b-math.sqrt(s))/(2*a)    
    return x1,x2

def inkq(x1,x2):
    if x1==x2:
        print('Phuong trinh co nghiem kep')
        print('x1=x2=',x1,sep='')
    elif x1!=x2:
        print('Phuong trinnh co 2 nghiem')
        print('x1=',x1,sep='')
        print('x2=',x2,sep='')

a,b,c=nhap()
ff=giaipt(a,b,c)
if ff!= None:
    x1,x2=giaipt(a,b,c)
    inkq(x1,x2) 





            
    