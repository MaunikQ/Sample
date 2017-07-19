a = []
for i in range(5):
	b = []
	for j in range(5):
		b.append(0)
	a.append(b)

for i in a:
	for j in i:
		print j,
	print "\n"

def dec2bin (num):
	rem = []
	for i in range(5):
		rem.append(num%2)
		num = num/2
	return rem[4], rem[3], rem[2], rem[1], rem[0]
		