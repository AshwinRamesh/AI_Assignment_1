# COMP3308 AI
# Assignment 1
# @author Ashwin Ramesh
# SID 311254012
import data_preprocessing
import naiveBayes
import random
import knearest
# Split the data into two arrays of each class
def split_classes (file_name):
	training_data = data_preprocessing.load_csv_data(file_name)
	training_data.pop(0) # remove top row
	print len(training_data)
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

def init_ten_fold_stratification(file_name):
	(class_one,class_zero) = split_classes(file_name)
	arrays = split_into_stratified_arrays(class_one, class_zero)
	return create_test_training_arrays(arrays)

def write_folds_to_file(folds,file_name):
	try:
		f = open(file_name,"w+")
		for x in xrange(10):
			if x == 0:
				f.write("fold%d\n" %(x))
			else:
				f.write("\nfold%d\n" %(x))
			for row in folds[x]:
				temp_row = str(row)
				temp_row = temp_row.replace("(","")
				temp_row = temp_row.replace(")","")
				temp_row = temp_row.replace("'","")
				f.write(temp_row+"\n")
	except:
		exit(1)

def compare_classifiers(read_file,write_file,k_value):
	(test_arrays,training_arrays) = init_ten_fold_stratification(read_file)
	write_folds_to_file(test_arrays, write_file)
	num_rows = 0
	total_k_nearest = 0
	total_n_bayes = 0
	for x in xrange(10): # For every Fold
		curr_n_bayes = 0
		curr_k_nearest = 0
		(class_zero,class_one) = naiveBayes.calculate_mean_sd(training_arrays[x])
		num_rows = num_rows + len(test_arrays[x])
		for row in test_arrays[x]: # for each item in the fold
			# Do Naive Bayes for all items in the fold
			(temp_bayes_result,naive_match) = naiveBayes.classify(row,class_zero,class_one)
			if naive_match == True: # if the classes match
				curr_n_bayes = curr_n_bayes + 1
			# Do K-Nearest for all items in the fold
			(temp_k_val,k_match) = knearest.classify(k_value,row,training_arrays[x])
			if k_match == True: # if the classes match
				curr_k_nearest = curr_k_nearest + 1

		total_n_bayes =total_n_bayes + curr_n_bayes
		total_k_nearest = total_k_nearest + curr_k_nearest
		curr_n_bayes = (curr_n_bayes * 100.0) / len(test_arrays[x])
		curr_k_nearest = (curr_k_nearest * 100.0) /len(test_arrays[x])

		print "Fold-%d\t\tK-Nearest(%d): %.2f%%\t\tN.Bayes: %.2f%%\t\tDifference: %.2f%%" %(x+1,k_value,curr_k_nearest,curr_n_bayes,abs(curr_k_nearest-curr_n_bayes)) # output string
	total_n_bayes = (total_n_bayes * 100.0) / num_rows
	total_k_nearest = (total_k_nearest * 100.0) / num_rows
	print "Total Folds\tK-Nearest(%d): %.2f%%\t\tN.Bayes: %.2f%%\t\tDifference: %.2f%%" %(k_value,total_k_nearest,total_n_bayes,abs(total_k_nearest-total_n_bayes)) # output string

def main():
	compare_classifiers("pima.csv", "pima-folds.csv",1)
	compare_classifiers("pima.csv", "pima-folds.csv",5)
	compare_classifiers("pima.csv", "pima-folds.csv",10)
if __name__ == "__main__":
	main()
