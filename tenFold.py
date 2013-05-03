# COMP3308 AI
# Assignment 1
# @author Ashwin Ramesh
# SID 311254012
import data_preprocessing
import random

# Split the data into two arrays of each class
def split_classes (file_name):
	training_data = data_preprocessing.load_csv_data(file_name)
	training_data.pop(0) # remove top row
	class_zero = []
	class_one = []
	for row in training_data:
		if (row[8] == "class1"):
			class_one.append(row)
		else:
			class_zero.append(row)
	random.shuffle(class_one)
	random.shuffle(class_zero)
	return class_one,class_zero # randomise the two lists and return it

# Split the two classes of arrays into 10 stratified arrays
def split_into_stratified_arrays(class_one,class_zero):
	stratified_arrays = [[] for x in xrange(10)]
	i = 0
	for row in class_one:
		if i == 10:
			i = 0
		stratified_arrays[i].append(row)
		i = i + 1
	i = 0
	for row in class_zero:
		if i == 10:
			i = 0
		stratified_arrays[i].append(row)
		i = i + 1
	return stratified_arrays

#
def create_test_training_arrays(stratified_arrays):
	training_arrays = [[] for x in xrange(10)]
	test_arrays = [[] for x in xrange(10)]
	for x in xrange(10): # for every training and test array
		for y in xrange(10): # for every stratified array
			if x == y:
				test_arrays[x].extend(stratified_arrays[y])
			else:
				training_arrays[x].extend(stratified_arrays[y])
	return test_arrays,training_arrays

def main():
	(class_one,class_zero) = split_classes("pima.csv")
	arrays = split_into_stratified_arrays(class_one, class_zero)
	(test_arrays,training_arrays) = create_test_training_arrays(arrays)
if __name__ == "__main__":
	main()
