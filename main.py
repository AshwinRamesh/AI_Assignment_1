# COMP3308 AI
# Assignment 1
# @author Ashwin Ramesh
# SID 311254012

import data_preprocessing
import knearest
import naiveBayes
import tenFold


def main():
	readFile = "pima-indians-diabetes.data"
	writeFile = "pima.cvs"
	data_preprocessing.doPreprocessing(readFile,writeFile)

	return 0;


if __name__ == "__main__":
	main()
