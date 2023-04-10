def add(L,x,k):
    if k<len(L):
        L=L.insert(k,x)
    else:
        L=L.append(x)

L=[1,2,'a','c','asd',45,123]
k=int(input('Vi tri them vao:'))
x=12
add(L,x,k)
print(L)



    
    