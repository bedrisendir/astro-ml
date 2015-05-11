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

#files=["node5C","node49","node43","node5E"]
#for file in files:
filename = "traingdata/node49.csv"
ll = pd.read_csv(filename)
ll = np.array(ll)
ll=ll[0:,3:]
ll=ll[0:,:-1]
ll=np.array(ll,dtype=np.float64)
ll=np.array(np.nan_to_num(ll))

componentCount=67 
sklearn_pca=sklearnPCA(n_components=componentCount) 
ll =sklearn_pca.fit_transform(ll) 

print ll.shape
print ll

#ll[np.isnan(ll)]=0

#print ll.shape

cov = np.cov(ll, rowvar=0)
mean = np.mean(ll, axis=0)

#cov = np.var(ll, 0)
cov = np.array(cov)
#mean = np.mean(ll, 0)
mean = np.array(mean)

#print cov
#print mean

#k = mean.shape[0]
#if len(cov.shape) == 1:
#       cov = np.diag(cov)

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

y = ss.multivariate_normal.logpdf(ll, mean, cov, allow_singular=True)
#print y
#print len(y)
#fig1 = plt.figure()
#ax = fig1.add_subplot(111)
#plt.plot(ll, y)
#y = multivariate_normal.pdf(ll, mean, cov)
#plt.plot(x,y,'x'); plt.axis('equal'); plt.show()
#print list(xrange(0,5856))
plt.hist(y,bins=15)
#df= pd.DataFrame(np.log(y))
#df["y"]=list(xrange(0,5856))
print y
#plt.figure();
#plt.hist(y,orientation='horizontal')
#df.plot(x=df["y"],y=df[0],kind='hist')
#print y[0]
#plt.plot(y)
#plt.plot(ss.rv_continuous.logpdf(y))
#plt.contourf(ll, y)
#plt.plot(y.T)
#print len(y)
#plt.plot(y)
plt.show()
