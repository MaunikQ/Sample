if __name__ == '__main__':
	email = raw_input('Please enter a user id: ')
	username = email.split('@')
	print ('The username of the email id is: '), username[0]