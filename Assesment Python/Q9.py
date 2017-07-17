def validate(s):
	min_length = max_length = digit = lower = upper = special = False
	if(len(s)>=6):
		min_length = True
	if(len(s)<=12):
		max_length = True
	
	if (("$" in s) or ("#" in s) or ("@" in s)):
		special = special or True

	for i in range(len(s)):
		if(s[i].isdigit()):
			digit = digit or True
		if(s[i].islower()):
			lower = lower or True
		if(s[i].isupper()):
			upper = upper or True
		
	
	if( min_length and max_length and lower and upper and digit and special):
		print 'Valid'
	else:
		print 'Not Valid'
	

if __name__ == '__main__':
	str = raw_input('Enter your password: ')
	validate(str)
