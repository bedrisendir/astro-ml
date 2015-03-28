import numpy as np

def scientificToFloat(array):
	
	convertedVersion = map("{0:.16f}".format, array)
	
	print convertedVersion
	
	
	
a = np.array([-2.75090260e-08, 3.11586226e-08, 1.86128266e-08, -1.01560789e-07])

scientificToFloat(a)
