import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import multivariate_normal

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

filename = "~/Desktop/astro-ml/Data-Preparation/testdata/node43out.csv"

ll = pd.read_csv(filename)
ll = np.array(ll)
#ll[np.isnan(ll)]=0

print len(ll[1])
print ll[1]
cov = np.cov(ll[1], rowvar=0)
cov = np.array(cov)
mean = np.mean(ll[1], axis=0)
mean = np.array(mean)
#print cov
#print mean

#x,y = np.random.multivariate_normal(mean,cov,111).T
#print x
#print y


y = multivariate_normal.pdf(ll[1], mean, cov)
print y
print len(y)
fig1 = plt.figure()
ax = fig1.add_subplot(111)
ax.plot(ll[1], y)
#y = multivariate_normal.pdf(ll, mean, cov)
#plt.plot(x,y,'x'); plt.axis('equal'); plt.show()
