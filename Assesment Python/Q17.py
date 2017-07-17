class Circle:
	def __init__(self, radius):
		self.radius = radius
	
	def area(self):
		print 'The area of the circle is: ', 3.14*(self.radius)*(self.radius)

if __name__ == '__main__':
	radius = int(input(('Enter the radius of the circle: ')))
	circle1 = Circle(radius)
	circle1.area()