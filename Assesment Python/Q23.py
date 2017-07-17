str = raw_input('Enter comma separated numbers: ')
seq = str.split(',')
l=[]
for i in range(len(seq)):
	l.insert(i,seq[i])
t = tuple(l)
print l
print t