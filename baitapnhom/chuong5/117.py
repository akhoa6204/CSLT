nx=[]
ny=[]
xy=[]
xbinh=[]

x=float(input('x='))
y=float(input('y='))

nx+=[x]
ny+=[y]
xy+=[x*y]
xbinh+=[x**2]

tieptuc=input('x=')
while tieptuc!='':
    tieptucx=float(tieptuc)
    tieptucy=float(input('y='))
    
    nx+=[tieptucx]
    ny+=[tieptucy]
    xy+=[tieptucx*tieptucy]
    xbinh+=[tieptucx**2]
    
    tieptuc=input('x=')

m = (sum(xy) - ((sum(nx) * sum(ny)) / len(nx)) )/ (sum(xbinh) - ((sum(nx) ** 2) / len(nx)))

b=(sum(ny)/len(ny))-m*(sum(nx)/len(nx))

print('y= '+str(round(m,2))+'x + '+str(round(b,2)))
