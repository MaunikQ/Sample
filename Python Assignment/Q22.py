l = [12,24,35,70,88,120,155]
print 'Original List: ', l
s=[]
for i in range(1,len(l),2):
	s.insert(i/2,l[i])
print 'Updated list with even index numbered removed: ', s