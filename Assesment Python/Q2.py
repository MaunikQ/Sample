a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

end_index = 0
str = ''
sum = 0
line_sum = []
i=0
for i in range(6):
	sum = sum + i
	line_sum.insert(i,sum);
	print line_sum

for i in range(len(line_sum)):
	for j in range(i+1):
		str = str + ' ' + a[line_sum[i]+j]	
	print str
	str=''