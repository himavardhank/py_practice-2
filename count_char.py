l="this is python"
d={}
for word in l.split():
	for ch in word:
		d[ch]=d.get(ch,0)+1
for k,v in d.items():
	    print('{} ocures {} times'.format(k,v))

