import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import scipy.stats as ss
from sklearn.decomposition import PCA as sklearnPCA

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

files=["node5C","node49","node43","node5E"]
for file in files:
    file = "traingdata/"+file+".csv"
    ll = pd.read_csv(file)
    ll = np.array(ll)
    ll=ll[0:,3:]
    ll=ll[0:,:-1]
    ll=np.array(ll,dtype=np.float64)
    ll=np.array(np.nan_to_num(ll))

    #APPLY PCA HERE
    componentCount=67
    sklearn_pca=sklearnPCA(n_components=componentCount)
    ll =sklearn_pca.fit_transform(ll)

    print ll.shape
    print ll
    # USE PCA RESULTS
    cov = np.cov(ll, rowvar=0)
    mean = np.mean(ll, axis=0)

    cov = np.array(cov)
    mean = np.array(mean)

    y = ss.multivariate_normal.logpdf(ll, mean, cov, allow_singular=True)
    plt.hist(y,bins=15)
    print y
    plt.show()
