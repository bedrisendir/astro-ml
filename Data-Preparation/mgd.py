import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
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

print ll.shape

cov = np.cov(ll, rowvar=0)
mean = np.mean(ll, axis=0)

#cov = np.var(ll, 0)
cov = np.array(cov)
#mean = np.mean(ll, 0)
mean = np.array(mean)

print cov
print mean

#k = mean.shape[0]
#if len(cov.shape) == 1:
#	cov = np.diag(cov)

#ll = ll - mean
#p = (2 * math.pi) ** (-k / 2) * np.linalg.det(cov) ** (-0.5) * np.exp(-0.5 * np.sum(np.dot(ll, np.linalg.pinv(cov)) * ll, 1))
#print p
#print cov
#print mean

#x,y = np.random.multivariate_normal(mean,cov,111).T
#print x
#print y

#x = np.linspace(0, 5, 10, endpoint=False)
#y = multivariate_normal.pdf(x, mean=2.5, cov=0.5)

y = multivariate_normal.pdf(ll, mean, cov, allow_singular=True)
print y
#print len(y)
fig1 = plt.figure()
ax = fig1.add_subplot(111)
ax.plot(ll, y)
#y = multivariate_normal.pdf(ll, mean, cov)
#plt.plot(x,y,'x'); plt.axis('equal'); plt.show()
