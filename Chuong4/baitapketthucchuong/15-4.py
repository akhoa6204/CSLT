def nhap():
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    return a,b,c

def max(a,b,c):
    max=a
    if max<b:
        max=b
    if max<c:
        max=c
    kq=max 
    return kq 

def inkq(kq):
    print('So lon nhat la:',kq)

a,b,c=nhap()
kq=max(a,b,c)
inkq(kq)