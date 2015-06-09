__author__ = 'xiangliu'
import kNN
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')
normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
print normMat
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], 15.0 * np.array(datingLabels), 15.0 * np.array(datingLabels))
# plt.show()