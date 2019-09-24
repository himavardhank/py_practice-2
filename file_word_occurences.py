#fname=input("enter file name")
k=0
f=open("abc.txt",'r')as f1:
    for line in f:
        words=line.split()
        for i in words:
            if(i==word):
                k+=1
print("no of occurences",k)
        
