a = raw_input('Enter first string: ')

for i in range (len(a)):
 	if(a[i] == a[len(a) - 1 -i]):
		i = i+1	
	else:
		break
if (i == len(a)):
	print('Palindrome')
else:
	print('Not a Palindrome')
	