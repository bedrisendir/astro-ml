#aim is to remove/handle all NaN values

#count NaN s for each column

#zero if all null data

#copy previous value if NaNs are rare

def handle(dataset):
	kv={}
	for column in dataset:
		count=0
		for data in dataset[column]:
			#if column == "ugi.ugi.loginFailure_avg_time":
			#	print data
			if data == "NaN":
				count+=1
		kv[column]=count

	for key in kv:
		if kv[key] != 0:
			print key , " " , kv[key]
	
