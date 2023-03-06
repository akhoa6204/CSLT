n=int(input('n='))
i=1
while 1<=n<=50:
    while i<=n:
        if i%10==0:
            print(i,end='\n')
        else: 
            print(i,end=' ')
        
        i+=1
        
    