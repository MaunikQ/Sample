

def main_func():
	d = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' , 'Sunday')
	m = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

	str = raw_input('Enter M for Month and W for Weekday: ')
	if (str == 'M' or str =='m'):
	
		month = raw_input('Enter a month: ')	
		if (month.title() in m):
			print m.index(month.title()) + 1
			val = raw_input('Wanna gain some more knowledge? Type Y for yes, anything else to exit: ')
			if(val == 'Y' or val =='y'):
				main_func()
			else:
				exit()
		else:
			print 'Are you kidding! No such month exist in a year! Try again'
			main_func()
		
	if (str == 'W' or str =='w'):
		day = raw_input('Enter a weekday: ')
		if (day.title() in d):	
			print d.index(day.title()) + 1
			val = raw_input('Wanna gain some more knowledge? Type Y for yes, anything else to exit')
			if(val == 'Y' or val =='y'):
				main_func()
			else:
				exit()
		else:
			print 'You must be joking! No such day exist in a week! Try again'
			main_func()

	else:
		print'Please enter a valid value! Try again!'
		main_func()


if __name__ == '__main__':
	main_func()

	


