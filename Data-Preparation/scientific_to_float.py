
import numpy as np
import writetoFile
import pandas as pd


def handle(dataset):
	
	count=0
	row = 0
	for column in dataset:
		count +=1
		if count>1 and column != "Date" and column != "Time" and column != "node":
			print count,"->",column
			dataset[column] = map("{0:.64f}".format, np.array(dataset[column],dtype=np.float64))			
	return dataset
	#dataset.to_csv("test.csv",float_format = '{:f}'.format,sep="\t",encoding='utf-8')	

		
	
		
		
		
	
	
#filename="master_dataset.csv"
#data=pd.read_csv("master_dataset.csv",dtype=str)

#handle(data)



