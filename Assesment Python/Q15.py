if __name__ == '__main__':
	t = []
	l=[]
	tuples = int(input('Enter the number of tuples to be inserted: '))
	size = int(input('Enter the size of each tuple: '))
	
	str = raw_input('Enter the numbers separated by space: ')
	str_seq = str.split(' ')
	int_str = list(map(int,str_seq))
	print int_str
	for i in range(tuples):
		for j in range(size):
			t.insert(j,int_str[i*size + j])
		l.insert(i,t)
		t=[]
	
	print l
		
	