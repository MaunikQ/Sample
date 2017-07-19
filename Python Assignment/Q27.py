t = (1,2,3,4,5,6,7,8,9,10)
print 'Given Input: ', t
s = []
j = 0
for i in range(len(t)):
	if(t[i] % 2 == 0):
		s.insert(j,t[i])
		j = j+1
print 'Even Numbers Tuple: ', tuple(s)