def nhap():
    n=int(input('n='))
    return n 
 
def inkq(n):
    for i in range (1,n+1):
        if i%2==0 :
            print(i,end=' ')
    print()

while True :   
    n=nhap()
    inkq(n)
    
    tieptuc=input('Tiep tuc khong?')
    if tieptuc=='k' or tieptuc=='K': 
        break
    elif tieptuc=='t': 
        continue 
    

    
    
    


        