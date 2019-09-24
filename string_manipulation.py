string=input("Enter string:")
count=0
#k=len(string)-1
for i in string:
      count=count+1
new=string[0:2]+string[count-2:count]
#new1=string[0:2]+string[k-1:count]
print("Newly formed string is:",new)
#print(new1)
