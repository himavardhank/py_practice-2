str1=['geeks,forgeeks','65.7492,62.5405','geeks,123','555.7492,152.5406']
temp=[]
for ele in str1:
    temp2=ele.split(',')
    temp.append((temp2))
output=[]
print(temp)
"""for ele in temp:
    temp3=[]
    for elem2 in ele:
        temp3.append(elem2)
    output.append(temp3)
print("###",output)"""
