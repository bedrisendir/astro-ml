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

    cov = np.cov(ll)
    mean = np.mean(ll)
    cov = np.array(cov)
    mean = np.array(mean)

    x = np.linspace(mean, cov, 100)
    print x
    ax.plot(x, norm.pdf(x), 'r-', lw=5, alpha=0.6, label='norm pdf')
    plt.show()