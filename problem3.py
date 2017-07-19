#Print max number of stars iteratiely and reverse
maxStars = int(input('Enter the max number of stars:'))
star = ''

for j in range(maxStars):
	star = star + '*'

for i in range(1,maxStars+1):	
	print star[:i]
	if(i==maxStars):
		for i in range(1,maxStars):
			print star[i:]
	
