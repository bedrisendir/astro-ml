#remove non changing metrics
import pandas as pd
def remove_constant(dataframe):
	columnNames=[]
	count=0
	smallCount=0
	titles = dataframe.columns.tolist()
	titles = titles[:-1]
	for title in titles:
		count +=1
                if count == 1 or count == 2 or count == 3:
                        continue
		l = dataframe[title]
		l = [float(i) for i in l]
		array_length = len(l)
		threshold = sum(l)/len(l)
		bigger=[]
		smallerAndEqual=[]
		smallCount=0
		for item in l:		
			if item <= threshold:
				smallCount +=1

		#print len(smallerAndEqual)
		#print len(bigger)
		if smallCount == len(l):
			#print "All data are equal"
			#print title
			columnNames.append(title)
	
	print "DeleteList:",columnNames
	for item in columnNames:
		del dataframe[item]

	
	return dataframe
