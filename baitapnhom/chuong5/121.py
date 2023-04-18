l=[]
n=int(input('n=(nhập 0 để dừng lại) '))
while n>0:
    l+=[n]
    n=int(input('n=(nhập 0 để dừng lại) '))
def countRange(l):
    max=int(input('max: '))
    min=int(input('min: '))
    s=0
    for i in l :
       if min<=i<=max:
           s+=1 
    return s
print(countRange(l))