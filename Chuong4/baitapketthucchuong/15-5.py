def NhapVaDem():
    print('Nhap day so:')
    kq=0
    while True:
        x=int(input())
        if SoHopLe(x):break 
        if LaSoNguyenTo(x):
            kq=kq+1
    return kq 
 
def SoHopLe(x):
    if x<=1: return True 
    else: return False

def LaSoNguyenTo(x):
    if x==2 : return True
    for i in range (2,x):
        if x%i==0: return False  
        else: u=True   
    return u 

def InKQ(kq):
    print ('Co',kq,'so nguyen to')
    
kq=NhapVaDem()
InKQ(kq) 
    
#return kết thúc vòng lặp 
#Nếu trả ra True thì chỉ cần nhập không cần để tương đương 

