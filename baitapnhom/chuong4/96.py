def nhap():
    i=input('MK:')
    return i 

def kiemthu(i):
    if len(i)>=8 and any(c.islower() for c in i) and any(c.isupper() for c  in i) and any(c.isdigit() for c in i):
#any(c.islower() for c in i) kiểm thử trong i có ít nhất 1 chữ cái thường k /upper là chữ cái hoa/digit là số 
        return True
    else:
        return False
def inkq():
    if kiemthu(i):print('Tot')
    else:print('Khong tot')        

while True :
    i=nhap()
    if kiemthu(i):
        inkq()
        break
    else: 
        inkq() 
        continue