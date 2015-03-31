# define thresholds for each column (small value)
# make sure that scientific notation handled
# get stdev of all columns
# stdevs compare with thresholds and remove the column
import numpy as np
def stdev(dataset):
    stdevlist={}
    for column in dataset:
        if column != "Date" and column != "Time" and column != "node":
            value=np.std(np.array(dataset[column],dtype=np.float64))
            stdevlist[column]=value
    #test=[]
    #for key in stdevlist:
    # 	test.append(stdevlist[key])

    #test=sorted(test)	
    #for i in test:
    #print i
    stdevlist2=sorted(stdevlist.items(),key=lambda num: num[1])    
    #print stdevlist2
    for item in stdevlist2:
	print item
    	#print stdevlist[item],"----------",item
    
    return dataset
