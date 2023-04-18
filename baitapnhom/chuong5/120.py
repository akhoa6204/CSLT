def kiemtra(l):   
    if len(l)==0 or len(l)==1:
        return True 
    tanglen=True
    giamxuong=True
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            tanglen=False
        elif l[i]<l[i+1]:
            giamxuong=False
        
    return tanglen or  giamxuong
l=[]
n=input()
while n!='':
    i=int(n)
    l=l+[i]
    n=input()
if kiemtra(l):
    print('True')
else: print('False')

        