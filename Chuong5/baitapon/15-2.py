def search(L,x):
    if x not in L: 
        print('None') 
    else: 
        print(L.index(x))
        
L=[1,2,3,4,5,6]
x=int(input('nhap x:'))
search(L,x)