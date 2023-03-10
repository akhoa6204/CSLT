n=int(input())
mahoa=['A','B','C','D','E','F','G','H','K','L']
#STT:0   1   2   3   4   5   6   7   8   9
while n>=0 and n<=9999:
    if n<10:
        print(mahoa[n])  
        #n=0,1,2,3,4,5,6,7,8,9 ứng với thứ tự trong mahoa 
        # vd:n=1 -> tt 1 tương ứng với 'B'
    elif n>=10 and n<100:
        print(mahoa[n//10],mahoa[n%10],sep='')
        #vd n =24: 
        #n//10: chia lấy phần nguyên: 24//10=2 -> tương ứng với 'C'
        #n%10=4: chia lấy phần dư: 24%10=4 -> tương ứng với 'E'
        #=> 24= CE
    elif n>=100 and n<1000:
        i=n//10 #vd: n=123 => i=12
        print(mahoa[i//10],mahoa[i%10],mahoa[n%10],sep='')
        #i//10=12/10=1 -> tương ứng với 'B'
        #i%10=12%10=2 -> tương ứng với 'C'
        #n%10=123%10=3 -> tương ứng với 'D'
    elif n>=1000 and n<=9999: #vd n=1234
        i=n//100 #i=n//100=1234//100=12
        j=n%100  #j=n%100=1234%100=34
        print(mahoa[i//10],mahoa[i%10],mahoa[j//10],mahoa[j%10],sep='')
    n=n*-1 # để kết thúc vòng lặp 
           # tại để ở vòng lặp while,for nên dùng để dừng while,for
           # nếu dùng không if thì k cần dùng lệnh n=n*-1 