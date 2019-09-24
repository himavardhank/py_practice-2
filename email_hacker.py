import re

N=int(input('enter num'))
emails =[]
for i in range(N):
    emails.append(input('enter email '))

pattern= re.compile('(^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{0,3}$)')    
print(sorted(filter(pattern.match,emails))) 




