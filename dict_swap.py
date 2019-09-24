d={'A': 67, 'B': 23, 'C': 45,'d':67}
new=dict([(value,key) for key,value in d.items()])
print("original dict",d)
print("after swapping",new)
