# The NumPy module also comes with a number of built-in routines for linear algebra calculations. These can be found in the sub-module linalg.
#
# linalg.det
#
# The linalg.det tool computes the determinant of an array.
#
# print numpy.linalg.det([[1 , 2], [2, 1]])       #Output : -3.0
# linalg.eig
#
# The linalg.eig computes the eigenvalues and right eigenvectors of a square array.
#
# vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
# print vals                                      #Output : [ 3. -1.]
# print vecs                                      #Output : [[ 0.70710678 -0.70710678]
#                                                 #          [ 0.70710678  0.70710678]]
# linalg.inv
#
# The linalg.inv tool computes the (multiplicative) inverse of a matrix.
#
# print numpy.linalg.inv([[1 , 2], [2, 1]])       #Output : [[-0.33333333  0.66666667]
#                                                 #          [ 0.66666667 -0.33333333]]
#
# Sample Input
#
# 2
# 1.1 1.1
# 1.1 1.1
# Sample Output
#
# 0.0

import numpy as np

a = int(input())
np.set_printoptions(legacy='1.13')
arr1 = np.array([input().split() for _ in range(a)]).astype(float)
print(np.linalg.det(arr1))

