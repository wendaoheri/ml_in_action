__author__ = 'xiangliu'
import numpy as np
import operator

def createDataSet():
	group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 1], [0, 0.1]])
	labels = ['A', 'A', 'B', 'B']
	return group, labels

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances ** 0.5
	sortedDistIndexs = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndexs[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]

def file2matrix(filename):
	fr = open(filename)
	arrayOLines = fr.readlines()
	numberOfLines = len(arrayOLines)
	returnMat = np.zeros((numberOfLines, 3))
	classLabelVector = []
	index = 0
	for line in arrayOLines:
		line = line.strip()
		listFromLine = line.split('\t')
		returnMat[index] = listFromLine[0: 3]
		classLabelVector.append(int(listFromLine[-1]))
		index += 1
	return returnMat, classLabelVector

def autoNorm(dataset):
	minVals = dataset.min(0)
	maxVals = dataset.max(0)
	ranges = maxVals - minVals
	normDataset = np.zeros(dataset.shape)
	m = dataset.shape[0]
	normDataset = dataset - np.tile(minVals, (m, 1))
	normDataset /= np.tile(ranges, (m, 1))
	return normDataset, ranges, minVals

def datingClassTest():
	hoRatio = 0.1
	datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
	normMat, ranges, minVals = autoNorm(datingDataMat)
	m = normMat.shape[0]
	numTestVecs = int(m * hoRatio)
	errorCount = 1.0
	for i in range(numTestVecs):
		classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, ], datingLabels[numTestVecs: m], 3)
		print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i])
		if classifierResult != datingLabels[i]:
			errorCount += 1.0
	print "the total error rate is : %f" % (errorCount / float(numTestVecs))

datingClassTest()