if __name__ == '__main__':
	
	str = raw_input('Enter the sequence separated by space: ')
	str_seq = str.split(' ')
	seq = list(map(int,str_seq))
	#seq = [6,6,12,18,30,48,78]
	if(seq[2] == seq[1] + seq[0]):
		additive = True
	else:
		additive = False
	for i in range(3,len(seq)):
		if (seq[i] == seq[i-1] + seq[i-2]):
			additive = additive and True
		else:
			additive = False
	print additive