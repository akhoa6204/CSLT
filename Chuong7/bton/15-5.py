n=str(input())
chucai=0
chuso=0
for i in n: 
    if i.isnumeric() :
        chuso+=1
    elif i.isalpha():
        chucai+=1
print('Chu cai:',chucai)
print('Chu so:',chuso)