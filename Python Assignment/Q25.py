str = raw_input('Enter a valid email address: ')
l = str.split('@')
m = l[1].split('.')
print 'The domain name is: ', m[0]
	