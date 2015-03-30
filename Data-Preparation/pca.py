rom sklearn.decomposition import PCA as sklearnPCA

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
def pcaData(dataframe):
        count=0
        titles = dataframe.columns.tolist()
        ll = []
        #titles2 = dataframe2.columns.tolist()
        #ll2 = []
        for title in titles:
                count +=1
                if count == 1 or count == 2:
                        continue

                l = dataframe[title]
                l = [float(i) for i in l]
                ll.append(l)
                #l2 = dataframe2[title]
                #l2 = [float(i) for i in l2]
                #ll2.append(l2)

        #print len(ll)
        return ll
filename = "~/python/test.csv"
filename1 = "~/python/test1.csv"
ll = pcaData(pd.read_csv(filename))
ll2  = pcaData(pd.read_csv(filename1))

ll = np.array(ll)
ll2 = np.array(ll2)

# 1
all_samples = np.concatenate((ll, ll2), axis=1)
assert all_samples.shape == (7, 40), "The matrix has not the dimensions 3x40"

sklearn_pca = sklearnPCA(n_components=2)
sklearn_transf = sklearn_pca.fit_transform(all_samples.T)
print sklearn_pca
''' 
plt.plot(sklearn_transf[0:20,0],sklearn_transf[0:20,1],\
     'o', markersize=7, color='blue', alpha=0.5, label='class1')
plt.plot(sklearn_transf[20:40,0], sklearn_transf[20:40,1],\
     '^', markersize=7, color='red', alpha=0.5, label='class2')
 
plt.xlabel('x_values')
plt.ylabel('y_values')
plt.xlim([-4,4])
plt.ylim([-4,4])
plt.legend()
plt.title('Transformed samples with class labels from matplotlib.mlab.PCA()')
 
plt.draw()
plt.show()
'''

