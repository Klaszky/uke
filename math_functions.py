def prime(num):
	eSet = [1]
	if num % 2 != 0:
		for i in range(3, (num/2) ,2):
			if num % i == 0:
				eSet.append(i)
			else:
				continue
	else:
		for i in range(2, (num/2)+1):
			if num % i == 0:
				eSet.append(i)
			else:
				continue
	if len(eSet) > 1:
		eSet.append(num)
		return eSet
	else:
		return "It seems that {} is prime.".format(num)


def primeGen(num):
	primes = [1, 2, 3]
	if num <= 3:
		return primes
	if num < 0:
		return "I don't do negitive numbers. Sorry"
	for i in range(5, num+1, 2):
		temp = []
		for x in range(3, (i/2), 2):
			if i % x == 0:
				temp.append(i)
				break
		if len(temp) == 0:
			primes.append(i)
	return primes


def primeFactor(num):
	if num == 1:
		return [1]
	primes = primeGen(num)
	primes.remove(1)
	primeFactors = []
	tracker = num
	while(tracker != 0 and tracker != 1):
		if tracker in primeFactors:
			primeFactors.append(tracker)
			break
		if tracker % 2 == 0:
			primeFactors.append(2)
			tracker /= 2
		else:
			for i in primes:
				if tracker % i == 0:
					primeFactors.append(i)
					tracker /= i
					break
				else:
					continue
	return primeFactors

def hCf(num1, num2):
	#Highest Common Factor
	set1 = primeFactor(num1)
	set2 = primeFactor(num2)
	commonFactors = []
	finalAnswer = 1
	for i in set1:
		if i in set2:
			commonFactors.append(i)
			set2.remove(i)
		else:
			continue
	for i in commonFactors:
		finalAnswer *= i
	return "Highest Common Factor: {}".format(finalAnswer)

	
def lCm(num1, num2):
	#Lowest Common Multiple
	set1 = primeFactor(num1)
	set2 = primeFactor(num2)
	factors = []
	finalAnswer = 1
	for i in set1:
		factors.append(i)
		if i in set2:
			set2.remove(i)
	for i in set2:
			factors.append(i)
	for i in factors:
		finalAnswer *= i
	factors.sort()
	#print "Factors: {}".format(factors)
	#return factors
	return "Lowest Common Multiple: {}".format(finalAnswer)

def lCm2():
	#Lowest Common Multiple
	set1, set2, set3, set4, set5, set6, set7, set8, set9, set10 = primeFactor(1), primeFactor(2), primeFactor(3), primeFactor(4), primeFactor(5), primeFactor(6), primeFactor(7), primeFactor(8), primeFactor(9), primeFactor(10)
	set11, set12, set13, set14, set15, set16, set17, set18, set19, set20 = primeFactor(11), primeFactor(12), primeFactor(13), primeFactor(14), primeFactor(15), primeFactor(16), primeFactor(17), primeFactor(18), primeFactor(19), primeFactor(20)
	sets = [
	set1, set2, set3, set4, set5, set6, set7, set8, set9, set10,
	set11, set12, set13, set14, set15, set16, set17, set18, set19, set20,
	]
	factors = []
	finalAnswer = 1
	for i in range(20):
		for item in sets[i]:
			factors.append(item)
			for x in range(20):
				if sets[i] > sets[x]:
					continue
				else:
					if item in sets[x]:
						sets[x].remove(item)
			# for 
		# if i in set2:
		# 	set2.remove(i)
	for i in factors:
		finalAnswer *= i
	factors.sort()
	print factors
	return "Lowest Common Multiple: {}".format(finalAnswer)

print lCm2()

