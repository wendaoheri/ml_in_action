__author__ = 'xiangliu'
from math import log


def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts = {}
	for featVec in dataSet:
		currentLabel= featVec[-1]
		if currentLabel not in labelCounts:
			labelCounts[currentLabel] = 1
		else:
			labelCounts[currentLabel] += 1
	shannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key]) / numEntries
		shannonEnt -= prob * log(prob, 2)
	return shannonEnt


def createDataSet():
	dataSet = [
		[1, 1, 'Yes'],
		[1, 1, 'Yes'],
		[1, 0, 'No'],
		[0, 1, 'No'],
		[0, 1, 'No']
	]
	label = ['no surfacing', 'flippers']
	return dataSet, label


def splitDataSet(dataSet, axis, value):
	retDataset = []
	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec = featVec[: axis]
			reducedFeatVec.extend(featVec[axis + 1:])
			retDataset.append(reducedFeatVec)
	return retDataset

dataMat, labels = createDataSet()
print splitDataSet(dataMat, 0, 0)