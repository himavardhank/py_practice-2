"""def swaplist(newlist):
    size=len(newlist)
    temp=newlist[0]
    newlist[0]=newlist[size-1]
    newlist[size-1]=temp
    return newlist
newlist=[12,35,9,56,24]
print(swaplist(newlist))"""

#############################

def swaplist(newlist):
	newlist[0],newlist[-1]=newlist[-1],newlist[0]
	return newlist
newlist=[12,35,9,56,24]
print(swaplist(newlist))
