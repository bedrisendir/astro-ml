import matplotlib.pyplot as plt
import numpy as np
mean = [0,0]
cov = [[1,0],[0,100]]
x,y = np.random.multivariate_normal(mean,cov,5000).T
print x
print y
print len(x)
print len(y)
print sum(x)/len(x)
print sum(y)/len(y)
plt.plot(x,y,'x'); plt.axis('equal'); plt.show()


mean = (1,2)
cov = [[1,0], [1,0]]
x = np.random.multivariate_normal(mean, cov, (3,3))
print x
