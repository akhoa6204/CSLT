def nhap():
    i=int(input('So luong mat hang:'))
    return i

def tinhtien(i):
    if i==1:
        gia=giadon
    elif i>1:
        gia=giadon+giathaydoi*(i-1)
    else :
        print('Nhap lai so luong mat hang can van chuyen >0')
        return None 
    return gia
def inkq(gia):
    print('Tong phi van chuyen=',gia)
    
while True:
    giadon=10.95
    giathaydoi=2.95
    i=nhap()
    ff=tinhtien(i)
    if ff!= None:
        gia=tinhtien(i)
        inkq(gia)
        
    