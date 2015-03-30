#aim is to remove/handle all NaN values

#count NaN s for each column

#zero if all null data

#copy previous value if NaNs are rare

def handle(dataset):
	kv={}
	for column in dataset:
		count=0
		for data in dataset[column]:
			if data == "NaN":
				count+=1
		kv[column]=count
	ky=[]
	for key in kv:
		if kv[key] < len(dataset[key])*15/100:
			ky.append(key)
			del kv[key]
	
	for key in ky:
		del dataset[key]
	
	dataset.fillna(0.0)	
	return dataset
