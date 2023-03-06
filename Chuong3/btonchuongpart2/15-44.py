a=float(input('a='))
b=float(input('b='))
ch=input('Toan tu:')
while ch=='+' or ch=='-' or ch =='*' or ch == '/' :
    if ch=='+':
        print(a,ch,b,'=',a+b,sep='')
        ch=input('Tiep tuc:')
    elif ch=='-':
        print(a,ch,b,'=',a-b,sep="")
        ch=input('Tiep tuc:')
    elif ch=='*':
        print(a,ch,b,'=',a*b,sep="")
        ch=input('Tiep tuc:')
    elif ch=='/' and b!=0:
        print(a,ch,b,'=',a/b)
        ch=input('Tiep tuc:')
        if ch=='t' or ch=='T':
          break