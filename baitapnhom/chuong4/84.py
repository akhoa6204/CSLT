def nhap():
    a=int(input())
    b=int(input())
    c=int(input())
    return a,b,c

def tinh(a,b,c):
    if a>c>b:
        trungvi=c
    elif a>b>c:
       trungvi=b
    elif b>a>c:
       trungvi=a
    elif b>c>a:
       trungvi=c
    elif c>a>b:
        trungvi=a
    elif c>b>a:
        trungvi=b
    return trungvi

def inkq(trungvi):
    print('Trung vi la:',trungvi)

a,b,c=nhap()
trungvi=tinh(a,b,c)
inkq(trungvi)

    
    