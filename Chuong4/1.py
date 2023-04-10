# def Nhap():
#     print('Nhap mot so nguyen:')
#     n=int(input('n='))
#     return n 
# def Tinh(n):
#     S=0
#     for x in range (1,n+1):
#         S=S+x
#     return S
# def InKQ(n,S):
#     print('Tong cua ',n,' so nguyen duong dau tien=',S,sep='')

# n=Nhap()
# S=Tinh(n)
# InKQ(n,S)    





# def hello():
#     print('Howdy!')
#     print('Howdy!!!')
#     print('Hello there.')
# hello()
# hello()
# hello()
# def show_number(m,n):
#     for i in range(m,n+1):
#         print(i)



# show_number(10,44)
# def show_number(m=1,n=10):
#     for i in range(m,n+1):
#         print(i)
# show_number(3,7)
# show_number(3,)
# show_number()
# def Nhap():
#     x=int(input('x='))
#     y=int(input('y='))
#     return x, y



# c, d=Nhap()
# print('Hai so nguyen da nhap=',c,d)
# def NhapBanKinh():
#     x=int(input("Ban kinh="))
#     return x

# def TinhChuVi(x):
#     PI = 3.14
#     ChuVi=x*PI
#     return ChuVi

# BanKinh=NhapBanKinh()
# ChuVi=TinhChuVi(BanKinh)
# print(ChuVi)
def spam(divideby):
    try:
        result = 42 / divideby
    except:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)

print(spam(1))
print(spam(0))