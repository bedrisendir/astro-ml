from sklearn.decomposition import PCA as sklearnPCA
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

def pcaData(dataframe):
        count=0
        titles = dataframe.columns.tolist()
	titles = titles[:-1]
        ll = []
        for title in titles:
                count +=1
                if count == 1 or count == 2 or count == 3:
                        continue

                l = dataframe[title]
                l = [float(i) for i in l]
                ll.append(l)

        return ll

filename = "~/python/node43.csv"
filename1 = "~/python/node49.csv"
#filename2 = "~/python/node49.csv"

ll = pcaData(pd.read_csv(filename))
ll2  = pcaData(pd.read_csv(filename1))
#ll3 = pcaData(pd.read_csv(filename2))
ll = np.array(ll)
ll2 = np.array(ll2)
#ll3 = np.array(ll3)
ll[np.isnan(ll)]=0
ll2[np.isnan(ll2)]=0
#ll3[np.isnan(ll3)]=0

numberOfDimension = 129

# 1
#all_samples = np.concatenate((ll, ll2), axis=1)
all_samples = ll2
'''
# 2
meanList=[]
for i in range(0, numberOfDimension):
	meanList.append(all_samples[i,:])
	#meanList.append(all_samples[i:i])
mean_vector = np.array(meanList)

# 3 a
scatter_matrix = np.zeros((numberOfDimension, numberOfDimension))
#for i in range(all_samples.shape[1]):
for i in range(all_samples.shape[1]):
    if(i % 100 == 0):
    	print i
    #scatter_matrix += (all_samples[:,i].reshape(numberOfDimension,1)\
    	#- mean_vector).dot((all_samples[:,i].reshape(numberOfDimension,1) - mean_vector).T)
    scatter_matrix += (all_samples[:,i].reshape(numberOfDimension,1)\
	- mean_vector).dot((all_samples[:,i].reshape(numberOfDimension,1) - mean_vector).T)
# 3 b
cov_mat = np.cov(meanList)

# 4
eig_val_sc, eig_vec_sc = np.linalg.eig(scatter_matrix)

eig_val_cov, eig_vec_cov = np.linalg.eig(cov_mat)

componentCount=0

for i in range(len(eig_val_sc)):
    eigvec_sc = eig_vec_sc[:,i].reshape(1,numberOfDimension).T
    eigvec_cov = eig_vec_cov[:,i].reshape(1,numberOfDimension).T

    assert eigvec_sc.all() == eigvec_cov.all(), 'Eigenvectors are not identical'
    if eig_val_sc[i] >= 1: componentCount +=1


print "COMPONENT COUNT ", componentCount
'''
componentCount = 72
#componentCount = 67
sklearn_pca = sklearnPCA(n_components=componentCount)
sklearn_transf = sklearn_pca.fit_transform(all_samples.T)
df= pd.DataFrame(data=sklearn_transf)
df.to_csv("result2.csv")

#print sklearn_transf
