def nhap():
    i=int(input('Nhap so m di:'))
    return i 
def tinhtien(i):
    if 0<i<140:
        gia=giacoban
    elif i>=140:
        if (i-139)%140==0:
            gia=giacoban+((i-139)//140)*giathaydoi
        else:
            gia=giacoban+((i-139)//140)*giathaydoi+giathaydoi
    else:
        print('So km phai >0')
        return None 
    return gia 
def inkq(gia):  
    print('Tong gia ve=',gia)
while True:
    giacoban=4
    giathaydoi=0.25    
    i=nhap()
    ff=tinhtien(i)
    if ff!=None:
        gia=tinhtien(i)
        inkq(gia)
    


     