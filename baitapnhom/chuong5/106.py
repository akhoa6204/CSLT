def nhap():
    n=int(input())
    l=[]
    while True:
        if n<=4:
            print('Nhap lai!!!\nTong so nhap vao >4')
        else: break 
        n=int(input())
    if n>4:    
        for i in range(1,n+1):
            l+=[int(input())]
    return l

def kiemtra(l):
    max=l[0]
    min=l[0]
    for i in range(len(l)):
        if l[i]>max:
            max=l[i]
        if l[i]<min:
            min=l[i]
    print(max,min)
    print(l)
    l.remove(max)
    l.remove(min)
    print(l)
l=nhap()
kiemtra(l)
    
    
             