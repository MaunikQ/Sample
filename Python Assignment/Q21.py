l = [12,24,35,24,88,120,155,88,120,155]
print 'Original set: ', l
set_l = set(set(l))
print 'Duplicates removed:',
for e in set_l:
	print e,
