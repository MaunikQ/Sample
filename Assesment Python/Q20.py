str = raw_input ('Enter your string: ')
sliced = str.split(' ')
dist = set(sliced)

freq = []
i = 0
for e in dist :
	freq.insert(i,(e,str.count(e)))
	i = i+1
print freq