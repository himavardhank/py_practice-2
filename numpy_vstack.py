import numpy as np
'''a=np.arange(6).reshape(3,2)
b=np.arange(6,12).reshape(3,2)
print(a,"\n",b)
print(np.vstack((a,b)))
print(np.hstack((a,b)))


c=np.arange(30).reshape(2,15)
print(c)
d=np.hsplit(c,3)
print(d[0])
print(d[1])
print(d[2])


res=np.vsplit(c,2)
print(res[1])


a=np.arange(12).reshape(3,4)
b=a>4
print(b)
print(a[b])
a[b]=-1#replacing with -1
print(a)


a=np.arange(12).reshape(3,4)
print(a)
for x in np.nditer(a,order='F',flags=['external_loop']):
    print(x)'''
b=np.arange(3,15,4).reshape(3,1)
print(b)
c=np.arange(3,15,6).reshape(1,1)
print(c)
for x,y in np.nditer([b,c]):#broadcasting
   print(x,y) 
