import numpy as np
import pylab as pl
from sklearn import svm

np.random.seed(0)

# create random dataset with 40 separable points
X = np.r_[np.random.randn(100, 2) - [2, 2], np.random.randn(100, 2) + [2, 2]]
Y = [0]*100 +[1]*100

#fit the model
clf = svm.SVC(kernel='linear')
clf.fit(X, Y)

print(X)
print(Y)

pl.scatter(X[:, 0], X[:, 1], c='black')
pl.axis('tight')
pl.show()


# get the separating hyperplane
w = clf.coef_[0]
a = -w[0]/w[1]
xx = np.linspace(-5, 5)
yy = a*xx - (clf.intercept_[0])/w[1]

# plot the parallels to the separating hyperplane that pass through the support vectors
b = clf.support_vectors_[0]
yy_down = a*xx + (b[1] - a*b[0])
b = clf.support_vectors_[-1]
yy_up = a*xx + (b[1] - a*b[0])
print ("w: ", w)
print ("a: ", a)

print ("support_vectors_: ", clf.support_vectors_)
print ("clf.coef_: ", clf.coef_)

# switching to the generic n-dimensional parameterization of the hyperplan to the 2D-specific equation
# of a line y=a.x +b: the generic w_0x + w_1y +w_3=0 can be rewritten y = -(w_0/w_1) x + (w_3/w_1)
# plot the line, the points, and the nearest vectors to the plane
pl.plot(xx, yy, 'k-')
#pl.plot(xx, yy_down, 'k--')
#pl.plot(xx, yy_up, 'k--')
pl.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=80, facecolors='none')
pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired)
pl.axis('tight')
pl.show()
