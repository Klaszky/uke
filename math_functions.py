from math import sqrt
#I wrote this years ago. It's really, really not good. It does however print out a list
#of the number's divisors if the number isn't prime.
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

#This was written In march 2017, it's a lot faster than it's the prime function above it that was written like 2-3 years ago. 
def isPrime(num = None):
	#Some quick tests to short cut the process
	if num == None:
		return "No number entered."
		return False
	if num == 0:
		return False
	if num < 0:
		print "By definition, primes are integers greater than one with no positive divisors besides one and itself. Negative numbers are excluded."
		return False
	if num < 4:
		return True

	#If it's divisible by 2 it ain't prime
	if num % 2 == 0:
		return False
	else:
		for i in xrange(3, int(sqrt(num))+1, 2):
			if num % i == 0:
				return False

	return True




def primeGen(num):
	primes = [1, 2, 3]
	if num <= 3:
		return primes
	if num < 0:
		return "I don't do negative numbers. Sorry"
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
	return "Highest Common Factor of {} and {}: {}".format(num1, num2, finalAnswer)

	
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

###Was written to solve a project euler problem. It's ugly but it works###
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

def quadraticFormula(a,b,c):
	"""solves:x=(-(b) + OR - sqrt(b**2 - 4*(a*c)))/2*a
	and returns two values."""
	#the program gets weird if you don't do the sqrt separate
	sqroot = sqrt(b**2 - (4*a*c))
	pos = (-b + sqroot)/(2*a)
	neg = (-b - sqroot)/(2*a)
	return pos, neg

def factors(*args):
	"""iterates through the args and spits out a list of
	their factos"""
	for i in args:
		print_set = []
		if i % 2 == 0:
			for x in xrange(1,(i/2)+1):
				if i % x == 0:
					print_set.append(x)
			print_set.append(i)
			print "The factors of {} are {}".format(i, print_set)
		else:
			for x in xrange(1,((i+1)/2)+1,2):
				if i % x == 0:
					print_set.append(x)
			print_set.append(i)
			print "The factors of {} are {}".format(i, print_set)

def highestPrimeFactor(num):
	"""used for finding the largest square number that can be
	factored out of a sqrt (example sqrt(48) would return 16
	which means you could factor out a 16 and be left with 4*sqrt(3)"""
	squares = [i**2 for i in range(2,int(sqrt(num))+1)]
	ans = 0
	for i in squares:
		if num % i == 0:
			ans = i
	if ans > 0:
		return "The largest square that's in {} is: {}".format(num,ans)
	else:
		return "There is no hidden square in {}".format(num)


if __name__ == "__main__":
	# print lCm(93,32)
	# print primeFactor(56)
	# print hCf(65,63)
	# print quadraticFormula(7,0,-14)
	# print isPrime(18014398777917439) #takes ~30seconds
	# print isPrime(70368760954879) #takes 1.8s
	#p rint prime(16785407) #For comparison this takes .7s for a much much smaller number
	# factors(63)
	# print highestPrimeFactor(175)
