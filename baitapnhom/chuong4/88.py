def nhap():
    a=float(input())
    b=float(input())
    c=float(input())
    return a,b,c

def kiemthu(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return True 
    else:
        return False
    
def inkq(a,b,c):
    if kiemthu(a,b,c): print('True')
    else: print('False')
    
a,b,c=nhap()
kiemthu(a,b,c)
inkq(a,b,c)