x=float(input('x='))
y=float(input('y='))
ch=str(input('Phep toan:'))
if ch=='+':
    print(x,ch,y,'=',x+y,sep='')
elif ch=='-':
    print(x,ch,y,'=',x-y,sep='')
elif ch=='*':
    print(x,ch,y,'=',x*y,sep='')
elif y !=0 and ch=='/':
    print(x,ch,y,'=',x/y,sep='')
else:
    print('Khong hop le')
    
    
    