"""

COMP3308 - AI
Assignment 1
@author Hugh Purnell <hugh.purnell@gmail.com>
SSID: 310181941

K-nearest neighbor classifier

"""

from heapq import heappush, heappop

num_attributes = 8

def distance_squared(a, b, dimension):
	d = float(0)
	for i in range(dimension):
		d+= (a[i] - b[i])**2
	return d

def classify(k, sample, training_data):
	distances = []
	class0_count = 0
	class1_count = 0

	for training_sample in training_data:
		dist = distances_squared(sample, training_sample, num_attributes)
		heappush(distances, (dist, training_sample) )

	for i in range(k):
		(_, training_sample) = heappop(distances)
		if training_sample[num_attributes] == "class0":
			class0_count++
		if training_sample[num_attributes] == "class1":
			class1_count++
	
	if class0_count > class1_count:
		return "class0"
	else 
		return "class1"



