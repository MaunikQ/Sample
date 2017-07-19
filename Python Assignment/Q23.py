str =  raw_input('Enter the numbers separated by space: ')
split_str = str.split(' ')
split_int = list(map(int,split_str))
sort_l = sorted(split_int)
print 'Numbers in sorted manner is: ', sort_l
key = int(input('Enter the key to be searched: '))
length = len(sort_l)
mid = (length + 1)/2
end = length - 1
start = 0
index = -1
while (start<=end):
	mid = (start+end) /2
	if(sort_l[mid] == key):
		index = mid
		break
	if(sort_l[mid]> key):
		end = mid-1
	else:
		start = mid+1

if(index == -1):
	print 'Key not found in the list!'
else:
	print 'Key found at index: ', index


	
