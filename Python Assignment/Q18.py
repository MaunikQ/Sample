str = raw_input('Enter the string: ')
newstr = []
for i in range(len(str)):
	newstr.append(str[(len(str))-1 - i])
print ''.join(newstr)
	