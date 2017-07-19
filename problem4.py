max = int(input('Enter the number of Fibonacci numbers to be printed:'))
a = []
a.append(0)
a.append(1)
i=2
while (i<max):
      	a.append(a[i-1] + a[i-2])
	print '0, 1, ', a[i]
	i = i+1
	