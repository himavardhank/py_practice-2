import pdb
def flatten(a):
    if a == []:
        return a
    if isinstance(a[0], list):
        return flatten(a[0]) + flatten(a[1:])
    return a[:1] + flatten(a[1:])
s=[[1],[1,3,5,[6,7]],[5]]
print("Flattened list is: ",flatten(s))
pdb.set_trace()
