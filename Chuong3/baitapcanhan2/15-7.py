# a
n=int(input())
i=1
giaithua=1
while n==0 :
    print('1')
    n=int(input())
while n>0 and i<=n:
    giaithua*=i
    i+=1  
print(giaithua)
n=int(input())
while n<0:
    break 
#b
n=int(input())
while n>=0:
    i=1
    giaithua=1
    if n>0:
        for i in range (1,n+1):
            giaithua*=i
        print(giaithua)
        n=int(input())
    elif n<0:
        break
    else:
        print('1')
        n=int(input())
 
        


