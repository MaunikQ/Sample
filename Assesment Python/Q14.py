def power_of_two(n):
	if(n==1):
		return True
	if(n%2==0):
		return power_of_two(n/2)
	else:
		return False

if __name__ == '__main__':
	num = int(input('Enter the number to be checked: '))
	power = power_of_two(num)
	print power