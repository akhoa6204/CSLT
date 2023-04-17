list=[]
print('Nhap 10 so nguyen')
while True:
    n=int(input())
    list= list + [n]
    if len(list)==10:
        break 
x=int(input('nhap x='))

#a c1)
# for i in list:
#     if i==5:
#        list[list.index(i)]=x 
# # dùng index để tìm kiếm vị trị mà tại i có giá trị =5
# print(list)

#a c2) 
# for i in range (len(list)):
#     if list[i]==5:
#         list[i]=x
# print(list) 

#b c1)
# new=[]
# for i in list:  
#     if i!=x:
#         new=new+[i]
# print(new)
#b c2)
# for i in list:
#     if i==x:
#         list.remove(i)
# print(list)


    
    
    