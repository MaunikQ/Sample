str = raw_input('Enter the string: ')
digits = letters = 0
for i in range(len(str)):
	indi = str[i]
	if((indi.isalnum() == True) and (indi.isdigit() == False)):
		letters = letters + 1
	if(indi.isdigit()):
		digits = digits + 1
print 'Letters:', letters
print 'Digits:', digits