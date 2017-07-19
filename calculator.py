def add(num1, num2):
	return float(num1) + float(num2)

def sub(num1, num2):
	return float(num1) - float(num2)

def mult(num1, num2):
	return float(num1)*float(num2)

def div(num1, num2):
	if (num2 == 0):
		div_error(num1)
	else:
		return float(num1)/float(num2)
		

def div_error(num1):
	print 'Cannot divide by zero! Try again!'
	num2 = float(input('Enter second number again: '))
	num3 = div(num1,num2)
	print_output(num3)

def print_output(num):
	print 'The required answer is: ', num
	msg = raw_input('Would you like to continue or exit? Type C for continue, anything else for Exit: ')
	if(msg == 'C'):
		main_calc()
	else:
		exit()	
	
def main_calc():
	oper = raw_input('What kind of operation would you like to do? Enter +, -, * or /: ')
	if(oper == '+' or oper == '-' or oper == '*' or oper == '/' ):
		num1 = float(input('Enter the first number: '))
		num2 = float(input('Enter the second number: '))
		
		if(oper == '+'):
			num3 = add(num1,num2)
			print_output(num3)
		if(oper == '-'):
			num3 = sub(num1,num2)
			print_output(num3)
		if(oper == '*'):
			num3 = mult(num1,num2)
			print_output(num3)
		if(oper == '/'):
			num3 = div(num1,num2)
			print_output(num3)
		
	else:
		print 'Please enter a valid charachter! Try again!'
		main_calc()
	
if __name__ == '__main__':
	main_calc()
