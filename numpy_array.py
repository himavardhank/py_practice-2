import numpy as np
'''a=np.array([5,6,9])
print(a[0])
a=np.array([[1,2],[3,4],[5,6]])
print(a.ndim)
print(a.itemsize)
print(a.dtype)
a=np.array([[1,2],[3,4],[5,6]],dtype=np.float64)
print(a.size)
print(a.shape)
a=np.array([[1,2],[3,4],[5,6]],dtype=np.complex)
print(a)

a=np.zeros((3,4))
print(a)


b=np.ones((3,4))
print(b)

c=np.arange(1,5)
print(c)

c=np.arange(1,5,2)
print(c)
d=np.linspace(1,5,10)
print(d)
d=np.linspace(1,5,5)
print(d)'''

a=np.array([[1,2],[3,4],[5,6]])
print(a.shape)
print(a.reshape(2,3))

print(a.ravel())
print(a)
print(a.max())
print(a.min())
print(a.sum(axis=0))#column
print(a.sum(axis=1))#row

