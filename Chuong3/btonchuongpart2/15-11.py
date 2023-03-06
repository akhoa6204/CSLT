n=int(input('n='))
i=1
for n in range (1,n+1):
    if n==0:
        print('0!=1')
    else:
        i*=n
print(n,'!=',i,sep='')

        
       