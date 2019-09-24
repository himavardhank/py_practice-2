from functools import reduce
test=[[2,3,5,8],[2,6,7,3],[10,9,2,3]]
res=list(reduce(lambda i,j:i&j,(set(x)for x in test)))
print("common ele",res)
