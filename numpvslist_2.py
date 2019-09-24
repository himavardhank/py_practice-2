import numpy as np
import time
import sys
size=100000
l1=range(size)
l2=range(size)

a1=np.arange(size)
a2=np.arange(size)

#list
start=time.time()
result=[(x+y)for x,y in zip(l1,l2)]
print("list",(time.time()-start)*1000)

#numpy
start=time.time()
result=a1+a2
print("numpy",(time.time()-start)*1000)
