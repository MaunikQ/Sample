if __name__ == '__main__':
	num = int(input('Enter the number: '))
	sum = digit = 0

	while num != 0:
		digit = num%10
		sum = sum + digit
		num = num/10
	print ('The sum is: '),sum

