"""

COMP3308 - AI
Assignment 1
@author Hugh Purnell <hugh.purnell@gmail.com>
SSID: 310181941

K-nearest neighbor classifier

"""

from heapq import heappush, heappop
import random

from data_preprocessing import * 

num_attributes = 8

def euclid_distance_squared(a, b, dimension):
	d = float(0)
	for i in range(dimension):
		d+= ( a[i] - b[i] ) **2
	return d

def classify(k, sample, training_data):
	distances = []
	class0_count = 0
	class1_count = 0

	for training_sample in training_data:
		dist = euclid_distance_squared(sample, training_sample, num_attributes)
		heappush(distances, (dist, training_sample) )

	for i in range(k):
		(_, training_sample) = heappop(distances)
		if training_sample[num_attributes] == "class0":
			class0_count+=1
		if training_sample[num_attributes] == "class1":
			class1_count+=1

	if class0_count > class1_count:
		return "class0"
	else :
		return "class1"

def main():
	training_data =  load_csv_data("pima.csv")
	training_data.pop(0) #pop the header off

	test_sample = training_data.pop(random.randint(0, len(training_data) - 1 ))

	#print "Test sample:", test_sample

	c = classify(10, test_sample, training_data)
	print "Classifier predicted: ", c, " Actual class: ", test_sample[num_attributes]

if __name__ == "__main__":
	main()
