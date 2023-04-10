def nhap():
    i=input('chuoi can nhap:')
    n=input('so khoang trang:')
    return i,n

def kt(i,n):
    print(' '*int(n)+ i +' '*int(n))
    
i,n=nhap()
kt(i,n)