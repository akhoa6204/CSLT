n=str(input())
i=['$','#','@']
if 6<=len(n)<=17 and any(c.islower()for c in n) and any(c.isupper() for c in n) and any(c.isdecimal() for c in n) and any(c for c in i ):
    print('True')
else: print("False")