string1=input("Enter first string:")
string2=input("Enter second string:")
count1=0
count2=0
for i in string1:
      count1=count1+1
for j in string2:
      count2=count2+1
print(count1,count2)
if(count1==count2):
    print("Both strings are equal.")
elif(count1<count2):
    print("smaller string is:",string1)
      
else:
      print("Larger string is:",string1)
      
