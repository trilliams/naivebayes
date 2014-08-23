naivebayes
==========
Naive bayesian classifying program for use with accept/reject. Takes in a Pandas DataFrame, stores its data for specified attributes, and uses it to make a naive bayes classifier. Currently works for discrete valued variables. Use NBC(sample,attributes,target) to generate the classifier as an NBC object. NBC also takes an optional argument for a smoothing constant. Then, using nbclassify(NBC,sample) will generate guesses for the sample based on the given attributes and target of the object.

Soon to come:  
-Functionality for nan values  
-Gaussian Naive Bayes methods for use with continuous variables  
-Accept/Reject methods for use with resampling

Dependencies:  
Pandas, Numpy

Summary:  
naivebayes is a set of classifying algorithms built for use with accept/reject resampling. It is intended to be functional for both discrete-valued attributes under standard naive bayes and continuous-valued ones under gaussian naive bayes. Using a sample from a prior distribution, it will allow you to resample a data set into one in line with the posterior distribution of the function.
