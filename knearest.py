"""

COMP3308 - AI
Assignment 1
@author Hugh Purnell <hugh.purnell@gmail.com>
SSID: 310181941

K-nearest neighbor classifier

"""

from heapq import heappush, heappop
import random

import data_preprocessing


def euclid_distance_squared(a, b, attributes):
	d = float(0)
	for i in attributes:
		d+= ( a[i] - b[i] ) **2
	return d

def convert_att_names_to_indexes(attributes):
	attribute_indexes = []
	for attribute_name in attributes:
		if attribute_name == "class":
			continue
		index = data_preprocessing.get_header().index(attribute_name)
		if index > -1:
			attribute_indexes.append(index)

	return attribute_indexes

def classify(k, sample, training_data, att_names = None):

	if att_names == None:
		att_names = data_preprocessing.get_header()

	attribute_indexes = convert_att_names_to_indexes(att_names)

	class_index = att_names.index("class")

	distances = []
	class0_count = 0
	class1_count = 0

	for training_sample in training_data:
		dist = euclid_distance_squared(sample, training_sample, attribute_indexes)
		heappush(distances, (dist, training_sample) )

	for i in range(k):
		(_, training_sample) = heappop(distances)
		if training_sample[class_index] == "class0":
			class0_count+=1
		if training_sample[class_index] == "class1":
			class1_count+=1

	if class0_count > class1_count:
		if sample[class_index] == 'class0':
			return 0,True
		return 0,False
	else:
		if sample[class_index] == 'class1':
			return 1,True
		return 1,False

def main():
	training_data =  data_preprocessing.load_csv_data("pima.csv")
	training_data.pop(0) #pop the header off

	test_sample = training_data.pop(random.randint(0, len(training_data) - 1 ))

	#print "Test sample:", test_sample

	(c,correctness) = classify(10, test_sample, training_data)
	print "Classifier predicted: ", c, " Correctness: ", correctness

if __name__ == "__main__":
	main()
