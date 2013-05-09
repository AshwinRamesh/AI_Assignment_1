# COMP3308 AI
# Assignment 1
# @author Ashwin Ramesh
# SID 311254012
from __future__ import division
import data_preprocessing
import math
import random


# convert a array of data into a dictionary of headers=>data Custom Headers is a subset of all the headers. It will return an associative array containing only those headers
def convert_array_to_dict(inputArray,custom_headers=False):
	headers = data_preprocessing.get_header()
	outputArray = {}
	for header in headers: # don't include class
		outputArray[header] = inputArray[headers.index(header)]
	if (custom_headers != False): # subset of headers given
		temp_output = {}
		for key in custom_headers:
			if key in outputArray:
				temp_output[key] = outputArray[key]
		outputArray = temp_output
	return outputArray

#Formated Printing of Mean and SD
def print_mean_sd(data,name):
	print_line = "%s"%(name)
	for key in data.keys():
		temp = "\n %s: %s" %(key,str(data[key]))
		print_line = print_line + temp
	return print_line

# Calculate the Mean and Standard Dev. for all columns. Returns array[array[mean,sd]*7] for each column.
def calculate_mean_sd(inputData,attr_names=False):
	if attr_names == False:
		headers = data_preprocessing.get_header() # headers to data
	else:
		headers = attr_names
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
		dictRow = convert_array_to_dict(row,attr_names)
		class_name = dictRow.pop("class")
		if class_name == "class1": # for class_one
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
		dictRow = convert_array_to_dict(row, attr_names)
		class_name = dictRow.pop("class")
		if class_name == "class1": # for class_one
			for key in dictRow.keys():
				class_one[key]['sd'] += math.pow((dictRow[key]-class_one[key]['mean']),2) # (xi - mean)^2
		else: # for class_zero
			for key in dictRow.keys():
				class_zero[key]['sd'] += math.pow((dictRow[key]-class_zero[key]['mean']),2)

	for header in headers[:-1]:
		class_zero[header]['sd'] = math.sqrt(class_zero[header]['sd']/class_zero['size']) # (total_sum/N)^1/2
		class_one[header]['sd'] = math.sqrt(class_one[header]['sd']/class_one['size'])

	return class_zero,class_one;

def PDF_math(attr_val,mean,sd):
	fraction_val = (1/sd) * math.sqrt(1/(2*math.pi))
	power_val = (-1) * (math.pow((attr_val-mean),2)) / (2*math.pow(sd,2))
	value = fraction_val * math.exp(power_val)
	return value

# Calculate the PDF value for a given mean and SD
def calculate_PDF(inputArray,class_zero,class_one,attr_names=False):
	if attr_names == False:
		headers = data_preprocessing.get_header()
	else:
		headers = attr_names
	pdf_array = {'class_zero':{},'class_one':{}}
	for header in headers[:-1]:
		pdf_array['class_zero'][header] = PDF_math(inputArray[header],class_zero[header]['mean'],class_zero[header]['sd'])
		pdf_array['class_one'][header] = PDF_math(inputArray[header],class_one[header]['mean'],class_one[header]['sd'])
	return pdf_array

# Classify a given dataSet. Requires the output of calculateMeanAndSD.
def classify(inputArray,class_zero,class_one,attr_names=False):
	if attr_names == False:
		headers = data_preprocessing.get_header()
	else:
		headers = attr_names
	inputArray = convert_array_to_dict(inputArray, attr_names)
	pdf_array = calculate_PDF(inputArray,class_zero,class_one,attr_names)
	test_one_val = float(class_one['size'])/float(class_one['size']+class_zero['size']) # total percentage of classOne
	test_zero_val =  float(class_zero['size'])/float(class_one['size']+class_zero['size']) # total percentage of classZero
	for header in headers[:-1]: # multiplying out the bayes value for 0 and 1
		test_one_val = test_one_val * pdf_array['class_one'][header]
		test_zero_val = test_zero_val * pdf_array['class_zero'][header]
	#print "one: %f zero: %f "%(test_one_val,test_zero_val)
	if ((test_one_val - test_zero_val) >= 0):
		if inputArray['class'] == 'class1': # return True if actual == calculated
			return 1,True # for Diabetic
		return 1,False
	else:
		if inputArray['class'] == 'class0': # return True if actual == calculated
			return 0,True
		return 0,False # for Non-Diabetic

def init_bayes(file_name,attr_names=False):
	training_data = data_preprocessing.load_csv_data(file_name,False)
	return calculate_mean_sd(training_data,attr_names)

def main():
	attr_names = ['plasma_glucose_concentration','bmi','diabetes_pedigree','age','class'] # For CFS
	(class_zero, class_one) = init_bayes("pima.csv")
	#print print_mean_sd(class_zero,"Class Zero")
	#print print_mean_sd(class_one, "Class One")

	data = data_preprocessing.load_csv_data("pima.csv")
	data.pop(0)
	count_correct = 0
	count_incorrect = 0
	for item in data:
		(a,out) =  classify(item, class_zero, class_one)
		if out == True:
			count_correct = count_correct + 1
		else:
			count_incorrect = count_incorrect + 1
	print "Correct: %d    Incorrect: %d" %(count_correct,count_incorrect)
	#print print_mean_sd(class_zero,"Class Zero")
	#print print_mean_sd(class_one, "Class One")


	#initBayes(training_data)
	return 1;

if __name__ == "__main__":
	main()
