   Khởi taọ List

1)  Sử dụng phép gán
    #vd
# numbers = [item for item in range(1,6)]
# print(numbers)
2)  Sử dụng cấu trúc For
    #vd1
# matrix = [ [x,x+1,x+2] for x in range(1,10,3) ]
# print(matrix)
    #vd2
# numbers = [item for item in range(1,6)]
# print(numbers)
3)  Phương pháp constructor List
    #vd
# char=list('python')
# print(char)

   Truy xuất các phần tử trong List

1) 
    a)  Số chỉ mục (index)
    #vd
# spam['khoa','ngọc','minh','nơ','ducanh','hongquan']
# spam[0] => 'khoa'
# spam[1] => 'ngọc'
# spam[2] => 'minh'
 Lưu ý : số index phải là số nguyên
    b)  List trong List
    #vd
#khoa=[['1','2','3'],['5','6']]
#khoa[0][1] =>['2']
    c)  Số chỉ mục âm (negative indexes)
# index=-1 sẽ tham chiếu đến phần tử cuối trong List
# index=2 là phần tử áp cuối
    #vd
# spam=['cat','chó']
# spam[-1] => ['chó']
2)  Truy xuất tập con trong List
    #vd
# abc['anh','em','nhu','cai','...']
# abc[0:2] =>['anh','em']
# abc[0:-1] =>['anh','em','nhu','cai']
    #vd2
# abc['anh','em','nhu','cai','...']
# abc[:2] =>['anh','em']
# abc[1:] =>['em','nhu','cai','...']
# abc[:] => ['anh','em','nhu','cai','...']
    
    Cập nhật giá trị cho phần tử trong List

1)  Sử dụng phép gán số
    #vd
# abc['anh','em','nhu','cai','...']
# abc[1]='khoa'
# abc => ['anh','khoa','nhu','cai','...']
# abc[2]=abc[1]
# abc => ['anh','khoa','khoa','cai','...']
# abc[-1]=12345
# abc => ['anh','khoa','khoa','cai',12345]

    Thao tác trên List

1)  Toán tử +
    #vd
# numbers=[1,2]
# numbers=numbers+[3,4]
# print(numbers) => [1,2,3,4]
2)  Toán tử *
    #vd
# numbers=[1,2]
# numbers=numbers * 2
# print(numbers) => [1,2,1,2]
3)  Toán tử in và not
    #vd
# myPets = ['Zophie', 'Pooka', 'Fat-tail']
# print('Enter a pet name:')
# name = input()
# if name not in myPets:
#   print('I do not have a pet named ' + name)
# else:
#   print(name + ' is my pet.')
4)  Hàm len(): Trả về chiều dài của List
    #vd
# spam=[1,2,3,4,5,6]
# len(spam) => 6
# matrix=[[1,2,3],[4,5,6]]
# len(matrix) => 2
# len(matrix[0]) => 3
5) Hàm max(),Hàm min()
# Hàm max(): Trả về phần tử có giá trị lớn nhất trong List
# Hàm min(): Trả về phần tử có giá trị bé nhất trong List
     #vd
# numbers = [5, 3, 8, 2, 9]
# print(max(numbers)) => 9
# print(min(numbers)) => 2
6) Xóa phần tử trong List với hàm del()
    #vd
# spam=[1,2,3,4,5]
# del(spam[2])
# print(spam) => [1,2,4,5]
# del(spam[1])
# print(spam) => [1,4,5]
7) Duyệt các phần tử trong List
    #vd
# students=["An","Binh","Lan","Thanh","Minh"]
# Cach 1
# for x in students:
# print(x ,end=", ")
# Cach 2
# for x in range(len(students)):
# print(students[x] ,end=", ")
# => An, Binh, Lan, Thanh, Minh
8)Bổ sung phần tử cho List
    #vd
# catNames = [] (Khởi tạo List rỗng)
# while True:
#     print('Enter the name of cat ' + str(len(catNames) + 1)
#         + ' (Or enter nothing to stop.):')
#     name = input()
#     if name == '':
#         break
#     catNames = catNames + [name] # list concatenation 
                            # (biến name đặt trong [])
                            # (Phương pháp thêm phần tử cộng(+))
# print('The cat names are:')
# for name in catNames:
# print(' ' + name)




