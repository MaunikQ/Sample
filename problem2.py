temp = int(input('Enter the Temperature (number only):'))
type = raw_input('Enter F for Temperature in Fahrenheit and C for Temperature in Celcius:')

if (type == 'F'):
	c = (temp-32)*float(5)/9
	print 'Temperature in Celcius is:',c
elif (type == 'C'):
	f = temp*(float(9)/5) + 32
	print 'Temperature in Fahrenheit is:', f
else:
	print 'Please enter the correct type of temperature'

	