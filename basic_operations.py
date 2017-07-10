import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c= a+b
print 'Addition: ', c
print 'Subtraction: ', a-b
print 'Multiplication: ', a*b
if(b!=0):
	print 'Division: ', a/b
else :
 	print 'Division not possible'