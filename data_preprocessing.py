"""

COMP3308 - AI
Assignment 1
@author Hugh Purnell <hugh.purnell@gmail.com>
SSID: 310181941

Data preprocessing and file access module

"""

import csv

csv_header = ["num_pregnant", "plasma_glucose_concentration", "diastolic_blood_pressure", "tricepts_skin_fold_thickness", "2hour_serum_insulin",
		"bmi", "diabetes_pedigree", "age", "class"]
num_attributes = 8

def load_csv_data(filename):
	data = []
	with open (filename,'rb') as csvfile:
		rows = csv.reader(csvfile, delimiter=',', quotechar=',')
		for row in rows:
			sample = []
			for attribute in row:
				sample.append(attribute)
			data.append(tuple(sample) )
	return data

def write_csv_data(filename, data):
	with open (filename, 'wb') as csvfile:
		writer = csv.writer(csvfile, delimiter=',', quotechar=',')
		for row in data:
			writer.writerow(row)

def normalise_value(v, minv, maxv):
	return (v - minv)/(maxv - minv)

def preprocess_data(raw_data):
	processed_data = []

	# normalise data
	attributes_min = {}
	attributes_max = {}

	# first we calculate the min and max values for each attribute
	for i in range (num_attributes): #
		maxv = float('-inf')
		minv = float('inf')
		for sample in raw_data:
			v = float(sample[i])
			maxv = max(maxv, v)
			minv = min(minv, v)
		attributes_min[i] = minv
		attributes_max[i] = maxv

	# rebuild the table starting with the header
	processed_data.append(csv_header)

	for sample in raw_data:
		normalised_sample = []
		for i in range (num_attributes):
			v = float(sample[i])
			v_normalised = normalise_value(v, attributes_min[i], attributes_max[i])
			normalised_sample.append(v_normalised)

		if sample[num_attributes] == "0":
			normalised_sample.append("class0")
		if sample[num_attributes] == "1":
			normalised_sample.append("class1")
		processed_data.append(normalised_sample)
	return processed_data


def main():
	d = load_csv_data("pima-indians-diabetes.data")
	print "Data loaded from pima-indians-diabetes.data"
	d = preprocess_data(d)
	print "Preprocessing complete"
	write_csv_data("pima.csv", d )
	print "Preprocessed data written to pima.csv"


if __name__ == "__main__":
	main()
