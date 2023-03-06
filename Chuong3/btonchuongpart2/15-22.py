n=int(input('n='))    
if n>1:
    for i in range (2,n):
        if n%i==0:
            print(n,'khong la SNT')
            break
    else:
        print(n,'la SNT')
else:
    print(n,'khong la SNT')  