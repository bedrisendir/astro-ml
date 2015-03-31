#aim is to remove/handle all NaN values

#count NaN s for each column

#zero if all null data

#copy previous value if NaNs are rare
import numpy as np
def handle(dataset):	
	kv={}
	for column in dataset:
		count=0
		for data in dataset[column]:
			if data == "NaN" or data == "nan":
				count+=1
		kv[column]=count
	ky=[]
	mykeys=kv.keys()
	print "Mykeys len:",len(mykeys)

	for key in mykeys:
		#print "-->",len(dataset[key])*15/100
		#if kv[key]>0:
		#	print kv[key]
		if kv[key] > (len(dataset[key])*5/100):
			ky.append(key)
			#del kv[key]
	#print len(ky)
	#print "check ",len(list(dataset.columns.values))
	print "DeleteList:",ky
	for key in ky:
		del dataset[key]
	
	#print "check ",len(list(dataset.columns.values))
	#dataset.fillna(0)	
	for column in dataset:
		 arr=dataset[column]
		 for i in range(0,len(arr)):
			if arr[i] == "NaN" or arr[i] == "nan":
				arr[i]="0.0"	
		 dataset[column]=arr
	#dataset[np.isnan(dataset)]=0
	#dataset = np.array(dataset)
	#dataset[np.isnan(dataset)]=0

	#print dataset
	return dataset
