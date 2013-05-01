# COMP3308 AI
# Assignment 1
# @author Ashwin Ramesh
# SID 311254012

import data_preprocessing
import math
from heapq import heappush, heappop
import random

# convert a array of data into a dictionary of headers=>data
def convert_array_to_dict(inputArray,headers):
	outputArray = {}
	for header in headers[:-1]: # don't include class
		outputArray[header] = inputArray[headers.index(header)]
	#print inputArray
	#print outputArray
	return outputArray

# Calculate the Mean and Standard Dev. for all columns. Returns array[array[mean,sd]*7] for each column.
def calculate_mean_sd(inputData):

	headers = data_preprocessing.get_header() # headers to data
	class_one = {} 	# People with Diabetes
	class_zero = {} 	# People without Diabetes

	# Prepare arrays with initial data
	for header in headers[:-1]:
		class_one[header] = {'mean':0,"sd":0}
		class_zero[header] = {'mean':0,"sd":0}
	else:
		class_one['size'] = 0
		class_zero['size'] = 0

	# Calculate Mean #
	for row in inputData:
		dictRow = convert_array_to_dict(row,headers)
		#break
		if row[8] == "class1": # for class_one
			for key in dictRow.keys():
				class_one[key]['mean'] += dictRow[key]
			class_one['size'] += 1 # increment
		else: # for class_zero
			for key in dictRow.keys():
				class_zero[key]['mean'] += dictRow[key]
			class_zero['size'] += 1 # increment

	for header in headers[:-1]:
		class_zero[header]['mean'] = class_zero[header]['mean']/class_zero['size']
		class_one[header]['mean'] = class_one[header]['mean']/class_one['size']

	# Calculate SD
	for row in inputData:
		dictRow = convert_array_to_dict(row, headers)
		if row[8] == "class1": # for class_one
			for key in dictRow.keys():
				class_one[key]['sd'] += math.pow((dictRow[key]-class_one[key]['mean']),2) # (xi - mean)^2
		else: # for class_zero
			for key in dictRow.keys():
				class_zero[key]['sd'] += math.pow((dictRow[key]-class_zero[key]['mean']),2)

	for header in headers[:-1]:
		class_zero[header]['sd'] = math.sqrt(class_zero[header]['sd']/class_zero['size']) # (total_sum/N)^1/2
		class_one[header]['sd'] = math.sqrt(class_one[header]['sd']/class_one['size'])

	return class_zero,class_one;

# Calculate the PDF value for a given mean and SD
def calculatePDF(value,colMean,colSD):
	return 1

# Probability of YES|NO for diabetes overall from dataset
def calculateProbabilities(data):
	return 1

def initBayes(inputData):
	prob = calculateProbabilities(1)
	meanSD_array = calculate_mean_sd(1)
	return 1

# Classify a given dataSet. Requires the output of calculateMeanAndSD.
def classify(dataSet,meanSD_array):
	return 1

def main():
	training_data = data_preprocessing.load_csv_data("pima.csv")
	training_data.pop(0) # remove top row
	(class_zero, class_one) = calculate_mean_sd(training_data)
	print "class0: " + str(class_zero)
	print "class1:  " + str(class_one)
	#initBayes(training_data)
	return 1;

if __name__ == "__main__":
	main()
