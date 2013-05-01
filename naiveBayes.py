# COMP3308 AI
# Assignment 1
# @author Ashwin Ramesh
# SID 311254012

import data_preprocessing
import math
from heapq import heappush, heappop
import random

csv_header = ["num_pregnant", "plasma_glucose_concentration", "diastolic_blood_pressure", "tricepts_skin_fold_thickness", "2hour_serum_insulin",
		"bmi", "diabetes_pedigree", "age", "class"]


# Hugh...
def calc_mean_sigma(input_data):
	attribute_means = []
	attribute_sums = []
	attribute_signma = []
	
	#sums
	for i in range( csv_header.len() - 1) #don't include class
		for sample in data:
			attribute_sums += sample[i]	
	# averages
	# sigmas
	

# Calculate the Mean and Standard Dev. for all columns. Returns array[array[mean,sd]*7] for each column.
def calculateMeanAndSD(inputData):
	valueArray = 	{'num_pregnant': {'mean': 0, "sd": 0},
			'plasma_glucose_concentration':{'mean': 0, "sd": 0},
			'diastolic_blood_pressure': {'mean': 0, "sd": 0},
			'tricepts_skil_fold_thickness': {'mean': 0, "sd": 0},
			'2hour_serum_insulin': {'mean': 0, "sd": 0},
			'bmi': {'mean': 0, "sd": 0},
			'diabetes_pedigree' :{'mean': 0, "sd": 0},
			'age':{'mean': 0, "sd": 0}
			}
	numRows = len(inputData) # number of data points
	# Calculate Mean #
	for row in inputData[:-1]:
		valueArray['num_pregnant']['mean'] =valueArray['num_pregnant']['mean'] + row[0]
		valueArray['plasma_glucose_concentration']['mean'] =valueArray['plasma_glucose_concentration']['mean'] + row[1]
		valueArray['diastolic_blood_pressure']['mean'] =valueArray['diastolic_blood_pressure']['mean'] + row[2]
		valueArray['tricepts_skil_fold_thickness']['mean'] =valueArray['tricepts_skil_fold_thickness']['mean'] + row[3]
		valueArray['2hour_serum_insulin']['mean'] =valueArray['2hour_serum_insulin']['mean'] + row[4]
		valueArray['bmi']['mean'] =valueArray['bmi']['mean'] + row[5]
		valueArray['diabetes_pedigree']['mean'] =valueArray['diabetes_pedigree']['mean'] + row[6]
		valueArray['age']['mean'] =valueArray['age']['mean'] + row[7]
	else:
		row = inputData[-1]
		valueArray['num_pregnant']['mean'] =(valueArray['num_pregnant']['mean'] + row[0])/numRows
		valueArray['plasma_glucose_concentration']['mean'] =(valueArray['plasma_glucose_concentration']['mean'] + row[1])/numRows
		valueArray['diastolic_blood_pressure']['mean'] =(valueArray['diastolic_blood_pressure']['mean'] + row[2])/numRows
		valueArray['tricepts_skil_fold_thickness']['mean'] =(valueArray['tricepts_skil_fold_thickness']['mean'] + row[3])/numRows
		valueArray['2hour_serum_insulin']['mean'] =(valueArray['2hour_serum_insulin']['mean'] + row[4])/numRows
		valueArray['bmi']['mean'] =(valueArray['bmi']['mean'] + row[5])/numRows
		valueArray['diabetes_pedigree']['mean'] =(valueArray['diabetes_pedigree']['mean'] + row[6])/numRows
		valueArray['age']['mean'] =(valueArray['age']['mean'] + row[7])/numRows

	# Calculate Standard Deviation #
	for row in inputData[:-1]:
		valueArray['num_pregnant']['sd'] =valueArray['num_pregnant']['sd'] + math.pow(row[0]-valueArray['num_pregnant']['mean'],2)
		valueArray['plasma_glucose_concentration']['sd'] =valueArray['plasma_glucose_concentration']['sd'] + math.pow(row[0]-valueArray['plasma_glucose_concentration']['mean'],2)
		valueArray['diastolic_blood_pressure']['sd'] =valueArray['diastolic_blood_pressure']['sd'] + math.pow(row[0]-valueArray['diastolic_blood_pressure']['mean'],2)
		valueArray['tricepts_skil_fold_thickness']['sd'] =valueArray['tricepts_skil_fold_thickness']['sd'] + math.pow(row[0]-valueArray['tricepts_skil_fold_thickness']['mean'],2)
		valueArray['2hour_serum_insulin']['sd'] =valueArray['2hour_serum_insulin']['sd'] + math.pow(row[0]-valueArray['2hour_serum_insulin']['mean'],2)
		valueArray['bmi']['sd'] =valueArray['bmi']['sd'] + math.pow(row[0]-valueArray['bmi']['mean'],2)
		valueArray['diabetes_pedigree']['sd'] =valueArray['diabetes_pedigree']['sd'] + math.pow(row[0]-valueArray['diabetes_pedigree']['mean'],2)
		valueArray['age']['sd'] =valueArray['age']['sd'] + math.pow(row[0]-valueArray['age']['mean'],2)
	else:
		row = inputData[-1]
		valueArray['num_pregnant']['sd'] = math.sqrt(((valueArray['num_pregnant']['sd'] + math.pow(row[0]-valueArray['num_pregnant']['mean'],2))/numRows))
		valueArray['plasma_glucose_concentration']['sd'] = math.sqrt(((valueArray['plasma_glucose_concentration']['sd'] + math.pow(row[0]-valueArray['plasma_glucose_concentration']['mean'],2))/numRows))
		valueArray['diastolic_blood_pressure']['sd'] = math.sqrt(((valueArray['diastolic_blood_pressure']['sd'] + math.pow(row[0]-valueArray['diastolic_blood_pressure']['mean'],2))/numRows))
		valueArray['tricepts_skil_fold_thickness']['sd'] = math.sqrt(((valueArray['tricepts_skil_fold_thickness']['sd'] + math.pow(row[0]-valueArray['tricepts_skil_fold_thickness']['mean'],2))/numRows))
		valueArray['2hour_serum_insulin']['sd'] = math.sqrt(((valueArray['2hour_serum_insulin']['sd'] + math.pow(row[0]-valueArray['2hour_serum_insulin']['mean'],2))/numRows))
		valueArray['bmi']['sd'] = math.sqrt(((valueArray['bmi']['sd'] + math.pow(row[0]-valueArray['bmi']['mean'],2))/numRows))
		valueArray['diabetes_pedigree']['sd'] = math.sqrt(((valueArray['diabetes_pedigree']['sd'] + math.pow(row[0]-valueArray['diabetes_pedigree']['mean'],2))/numRows))
		valueArray['age']['sd'] = math.sqrt(((valueArray['age']['sd'] + math.pow(row[0]-valueArray['age']['mean'],2))/numRows))
	print valueArray

	return valueArray

# Calculate the PDF value for a given mean and SD
def calculatePDF(value,colMean,colSD):
	return 1

# Probability of YES|NO for diabetes overall from dataset
def calculateProbabilities(data):
	return 1

def initBayes(inputData):
	prob = calculateProbabilities(1)
	meanSD_array = calculateMeanAndSD(1)
	return 1

# Classify a given dataSet. Requires the output of calculateMeanAndSD.
def classify(dataSet,meanSD_array):
	return 1

def main():
	training_data = data_preprocessing.load_csv_data("pima.csv")
	training_data.pop(0) # remove top row
	calculateMeanAndSD(training_data)
	#initBayes(training_data)
	return 1;

if __name__ == "__main__":
	main()
