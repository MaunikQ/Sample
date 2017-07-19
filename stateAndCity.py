d = {'Mumbai':'Maharashtra', 'Bangalore' : 'Karnataka', 'Delhi' : 'Delhi', 'Chennai': 'Tamil Nadu', 'Kolkata': 'West Bengal', 'Surat' : 'Gujarat'}
type = raw_input('Enter c for City, s for state: ')
city = raw_input('Enter the name: ')

if type == 'c': 
	print 'The city is in the state: ', d[city.title()]
else:
	print 'The states city is: ', d[city.title()]
