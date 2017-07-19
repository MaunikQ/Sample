str = raw_input ('Enter the string: ')
l = str.split(' ')
digit = []
for i in range(len(l)):
	if(l[i][0].isdigit()):
		dig = True
	else:
		dig = False	
	
	for j in range(1,len(l[i])):
		if(l[i][j].isdigit()):
			dig = dig and True
		else:
			dig = False
	if(dig == True):
		print l[i],
	