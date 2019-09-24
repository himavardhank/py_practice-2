def fibb(n):
    if n<=1:
        return n
    else:
        return(fibb(n-1)+fibb(n-2))
num=int(input("enter how many numbers"))
if num<=0:
    print("pls enter valid num")
else:
    for i in range(num):
        print(fibb(i))
