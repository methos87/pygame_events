#!/usr/bin/env python

# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

from scipy import sparse

x = np.linspace(-10, 10, 100)
y = np.sin(x)
z = np.array([[1, 2, 3], [4, 5, 6]])

print("z:\n {}".format(z))

eye = np.eye(4)

print("\nplotting:")
plt.plot(x, y, marker="x")

print("\nNumPy array:\n{}".format(eye))

sparse_matrix = sparse.csr_matrix(eye)
print("\nSciPy sparse CSR matrix\n{}".format(sparse_matrix))

data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print("\nCOO representation:\n{}".format(eye_coo))
