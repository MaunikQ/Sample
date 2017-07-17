def func(num):
	print num,
	if(num==1):
		return -1;
	if(num%2 == 0):
		func(num/2)
	if(num%2 != 0):
		func((num*3) + 1)
	
if __name__ == '__main__':
	num = int(input('Enter the first number: '))
	func(num)