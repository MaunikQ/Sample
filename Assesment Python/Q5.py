def find_missing_num (num_list):
	n = len(num_list)
	sum = 0
	list_sum = 0
	for i in range(n):
		sum = sum + (i+1)
		list_sum = list_sum + num_list[i]
	if(list_sum != sum):
		return (num_list[i] - (list_sum-sum))
	else:
		return -1

if __name__ == '__main__':
	A = [1,2,3,4,5,6,7,9]
	missing = find_missing_num(A)
	if(missing != -1):
		print missing
	else:
		print ('No number was missing in the input list!')