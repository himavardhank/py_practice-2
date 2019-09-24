def countlist(lst):
    count=0
    for el in lst:
        if type(el)==type([]):
            count+=1
    return count
lst=[[1,2,3],[4,5],[],[6,7,8,9]]
print(countlist(lst))
