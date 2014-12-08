# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

%pylab inline

# <codecell>

import sklearn as sk
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt

# <headingcell level=1>

# Principal Components Analysis

# <headingcell level=3>

# Dimensionality Reduction and Visualization

# <headingcell level=6>

# #Get the digits data

# <codecell>

from sklearn.datasets import load_digits
digits = load_digits()

# <headingcell level=6>

# #What does the digits dataset contain?

# <codecell>

print digits.keys()

# <headingcell level=6>

# #Each row of data in X_digits corresponds to one of the following digits:

# <codecell>

digits.target_names

# <codecell>

X_digits, y_digits = digits.data, digits.target

# <headingcell level=6>

# #What does the X matrix look like?

# <codecell>

X_digits.shape

# <headingcell level=6>

# #Get the first 10 principal components of the X_digits matrix

# <codecell>

from sklearn.decomposition import PCA

estimator = PCA(n_components=10)
X_pca = estimator.fit_transform(X_digits)

# <headingcell level=6>

# #What does the PCA matrix looks like

# <codecell>

X_pca.shape

# <codecell>

X_pca

# <headingcell level=6>

# #Visualize our data using the first two principal components in a scatterplot

# <codecell>

colors = ['black', 'blue', 'purple', 'yellow', 'white', 'red', 'lime', 'cyan', 'orange', 'gray']
for i in xrange(len(colors)):
    px = X_pca[:, 0][y_digits == i]
    py = X_pca[:, 1][y_digits == i]
    plt.hexbin(px, py, c=colors[i])
plt.legend(digits.target_names)
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')

# <codecell>


