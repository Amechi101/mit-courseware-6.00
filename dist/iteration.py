# n = 5 #This stores the value
# n = 3 * n + 1 #This refers to the new Value 

# Intialize the value
# runs_scored = 0

# runs_scored = runs_scored + 1
# runs_scored += 1


def my_sum(xs):
	"""Sum all the numbers in the list xs, and return the total"""

	running_total = 0
	for x in xs:
		running_total += running_total + x

	return running_total

# While Statement

# This function means while v is less than or equal to n
# continue executing the body loop. Within the body ech time, increment
# v. When v passes n, accumulated sum
def sum_to_while(n):
	"""return the sum of 1 + 2+ 3 ...n"""
	ss = 0
	v = 1
	while v <= n:
		ss += v
		v += 1
	return ss

print sum_to_while(80)


# Using a for loop
def sum_t_for(n):
	"""return the sum of 1 + 2+ 3 ...n"""

	accumulated_num = 0
	for v in range(n+1):
		accumulated_num += v
	return accumulated_num 

print sum_t_for(3)

# The Collatz 3n + 1 Sequence

# "computational rule” for creating the sequence is to start from some given n, and to generate
# the next term of the sequence from n, either by halving n, (whenever n is even), or else
# by multiplying it by three and adding 1. The sequence terminates when n reaches 1.

def sequence3np1(n):
	"""Print the 3n + 1 from n, terminating when it reaches 1."""

	# Using the argument n within the function
	while n != 1:
		print (n, end =", ")

		if n % 2 == 0:
			n = n // 2
		else:
			n = n * 3 + 1
	print (n, end=" .\n")








