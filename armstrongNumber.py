max = 1000
sum = 0

for i in range(max):
	k = i
	digits = 1
	while k/10 != 0: 		
		digits = digits + 1
		k = k/10
        
	k = i
	while k!= 0:
        	j = k%10
		sum = sum + j**digits
		k = k/10		
        if sum == i:
		print i
 