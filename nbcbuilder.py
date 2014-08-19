import pandas as pd
import numpy as np
import random
import math

def classifier(sample,attributes,target):
    n = 0
    attributes = attributes
    classes = {}
    for label in set(sample[target]):
        classes[label] = {}
        for attribute in attributes:
            subsample = sample[sample[target]==label]
            classes[label][attribute]=\
                [sample[attribute][i] for i in subsample[attribute].index]
    return classes

def nbctrainer(sample,attributes,target,l=0):
    #training program for naive bayes classification
    #for smoothing, set l to an integer greater than zero
    if type(l)!=int:
        assert False, "l must be a nonnegative integer"
    classes0,classes1 = classifier(sample,attributes,target)

def findys(NBC,sample,attributes,target):
    NBC.ys = {}
    total = float(len(sample))
    for label in set(sample[target]):
        NBC.ys[label] = len(sample[sample[target]==label])/total
    return NBC.ys

def findthetas(NBC,sample,attributes,target):
    for keylabel in NBC.classes.keys():
        NBC.thetas[keylabel] = {}
        for attribute in NBC.attributes:
            NBC.thetas[keylabel][attribute] = {}
            for point in NBC.thetas[keylabel][attribute]:
                NBC.thetas[keylabel][attribute] = \
                        NBC.thetas[keylabel][attribute].get(point,0) + 1

def nbcprob(NBC,point):
    product = 1
    #multiply by probability of y
    product *= NBC.ys[point[NBC.target]]
    for attribute in NBC.attributes:
        product *= NBC.thetas[point[NBC.target]][attribute][point[attribute]]
    return product

def thetaprob(NBC,point):
    ##Used for finding probabilities of points where target value isn't known
    product = 1
    for attribute in NBC.attributes:
        product *= NBC.thetas[point[NBC.target]][attribute][point[attribute]]
    return product

def classprob(NBC,label,point):
    ##Used for finding probabilities of points where target value isn't known
    product = 1
    product *= NBC.ys[label]
    for attribute in NBC.attributes:
        product *= NBC.thetas[label][attribute][point[attribute]]
    return product

def nbcclassify(NBC,sample):
    if type(sample) == pd.Series:
        return nbcpoint(NBC,sample)
    elif type(sample) == pd.DataFrame:
        return [nbcpoint(NBC,sample.ix[i]) for i in sample.index]
    else:
        pass
        print "Sample must be a Pandas DataFrame or a point in one"

def nbcpoint(NBC,point):
    ##NBC for a point
    guess = None
    guessprob = 0
    for label in NBC.classes.keys():
        prob = classprob(NBC,label,point)
        if prob >= guessprob:
            guessprob = prob
            guess = label
    return guess

    
