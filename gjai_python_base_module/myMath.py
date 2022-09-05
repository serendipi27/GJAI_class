import math

pi = math.pi

def sum1toN(endNum):
	num = 0
	for i in range(1, endNum+1):
		num += i
	return num

def multi1toN(endNum):
	num = 1
	for i in range(1, endNum+1):
		num *= i
	return num
