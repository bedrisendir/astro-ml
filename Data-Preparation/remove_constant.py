#remove non changing metrics
def remove_constant(list):
	array_length = len(list)
	threshold = sum(list)/len(list)
	print array_length
	print threshold
	bigger=[]
	smallerAndEqual=[]
	for item in list:		
		if item <= threshold:
			smallerAndEqual.append(item)
		else:
			bigger.append(item)

	print len(smallerAndEqual)
	print len(bigger)
	if len(smallerAndEqual) == len(list):
		print "All data are equal"

remove_constant([1,2,3,4,5])
remove_constant([1,1,1,1,1])
