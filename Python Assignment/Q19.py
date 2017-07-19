str = raw_input('enter the string: ')
str_set = set(str)
l =[]
i=0
for e in str_set:
	l.insert(i,(e,str.count(e)))
	i=i+1
print l
