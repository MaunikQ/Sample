class Str:
	def __init__(self):
		self.str = raw_input('Enter the string: ')
	
	def display(self):
		print 'The entered String is: ' ,self.str

if __name__ == '__main__':
	str1 = Str()
	str1.display()