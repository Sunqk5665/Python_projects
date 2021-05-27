def binaryInsert(series,a):
	low = 0
	high = len(series) - 1
	m = (low + high)//2
	while low < high:
		if series[m] > a:
			high = m - 1
		elif series[m] < a:
			low = m + 1
		else:
			high = m
		m = (low + high)//2
	series.insert(high+1,a)

l = sorted([2,4,7,3,9,1,5,6,9])
binaryInsert(l,5)
print(l)
