import numpy as np
def write(dataset,file):
	dataset.to_csv(file,sep='\t',dtype=np.float64,index=False)
