import datetime

def validate(date):
	d, m, y = date.split('-')
	try:
		datetime.datetime(year=y, month=m, day=d)
	except ValueError:
		raise ValueError ("Incorrect date format, should be DD-MM-YYYY")

if __name__ == '__main__':
	
	date = raw_input('Enter the date in format DD-MM-YYYY : ')
	validate(date)

	


	#time = raw_input('Enter the time in format HH:MM:SS : ')


	print d,m,y