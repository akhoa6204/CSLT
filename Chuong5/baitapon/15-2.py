def search(L,x):
    for i in range(len(L)):    
        if L[i]==x :
            print('Vi tri cua x la:',i)
            
    if x not in L : 
        print('None')
L=[]
n=int(input())
while True:
    i=int(input())
    L+=[i]
    if len(L)==n:
        break
x=int(input('nhap x='))
search(L,x)