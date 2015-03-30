from sklearn.decomposition import PCA as sklearnPCA

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
assert all_samples.shape == (5, 40), "The matrix has not the dimensions 3x40"

# 2
mean_x = np.mean(all_samples[0,:])
mean_y = np.mean(all_samples[1,:])
mean_z = np.mean(all_samples[2,:])
mean_t = np.mean(all_samples[3,:])
mean_w = np.mean(all_samples[4,:])
mean_vector = np.array([[mean_x],[mean_y],[mean_z],[mean_t],[mean_w]])

print('Mean Vector:\n', mean_vector)

# 3 a
scatter_matrix = np.zeros((5,5))
for i in range(all_samples.shape[1]):
    scatter_matrix += (all_samples[:,i].reshape(5,1)\
         - mean_vector).dot((all_samples[:,i].reshape(5,1) - mean_vector).T)
print('Scatter Matrix:\n', scatter_matrix)

# 3 b
cov_mat = np.cov([all_samples[0,:],all_samples[1,:],all_samples[2,:], all_samples[3,:], all_samples[4,:]])
print('Covariance Matrix:\n', cov_mat)

# 4
# eigenvectors and eigenvalues for the from the scatter matrix
eig_val_sc, eig_vec_sc = np.linalg.eig(scatter_matrix)

# eigenvectors and eigenvalues for the from the covariance matrix
eig_val_cov, eig_vec_cov = np.linalg.eig(cov_mat)

componentCount=0

for i in range(len(eig_val_sc)):
    eigvec_sc = eig_vec_sc[:,i].reshape(1,5).T
    eigvec_cov = eig_vec_cov[:,i].reshape(1,5).T
    assert eigvec_sc.all() == eigvec_cov.all(), 'Eigenvectors are not identical'

    print('Eigenvector {}: \n{}'.format(i+1, eigvec_sc))
    print('Eigenvalue {} from scatter matrix: {}'.format(i+1, eig_val_sc[i]))
    if eig_val_sc[i] >= 1: componentCount +=1
    print('Eigenvalue {} from covariance matrix: {}'.format(i+1, eig_val_cov[i]))
    print('Scaling factor: ', eig_val_sc[i]/eig_val_cov[i])
    print(40 * '-')



print "COMPONENT COUNT ", componentCount


sklearn_pca = sklearnPCA(n_components=2)
sklearn_transf = sklearn_pca.fit_transform(all_samples.T)
print sklearn_transf
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

