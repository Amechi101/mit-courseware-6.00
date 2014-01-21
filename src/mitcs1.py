# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
#---------------------------------

# Retrieve user input.

# Initialize some state variables. Remember to find the monthly interest rate from the annual interest rate taken in as input.

# For each month:
# o Compute the new balance. This requires computing the minimum monthly payment and figuring out how much will be paid to interest and how much will be paid to the principal.
# o Update the outstanding balance according to how much principal was paid off.
# o Output the minimum monthly payment and the remaining balance.
# o Keep track of the total amount of paid over all the past months so far.

# Print out the result statement with the total amount paid and the remaining balance.

#program scrap		

# balance = int(raw_input('What is your starting outstanding balance? '))  
	# apr = float(raw_input('APR on card? '))  #constant
		# min_month_pay_rate = float(raw_input('what is your minimum % \PR: '))


		# min_month_pay = round((balance * min_month_pay_rate))

		# principal_pay = round((apr/12 * balance))

		#  = round((balance - principal_pay))

		# print '''
		# minimum monthly pay: %r  
		# Principal Paid: %s 
		# Remaining balance: %d 
		# ''' % (min_month_pay, principal_pay, remaining_b)



# Program start below
balance = int(raw_input('What is your starting outstanding balance? '))  
apr = .18  #constant
min_month_pay_rate = .02 # constant

def month_1(min_month_pay, principal_pay, remaining_b):


	min_month_pay = round((balance * min_month_pay_rate))
	principal_pay = round((apr/12 * balance))
	remaining_b = round((balance - principal_pay))
    	print '''For month #1, minimum monthly pay: %r  Principal Paid: %s Remaining balance: %d ''' % (min_month_pay, principal_pay, remaining_b)

month_1('min_month_pay', 'principal_pay', 'remaining_b')


balance = int(raw_input('What is your starting outstanding balance? '))  

# start month 2

def month_2(min_month_pay, principal_pay, remaining_b):
	min_month_pay = round((balance * min_month_pay_rate))
	principal_pay = round((apr/12 * balance))
	remaining_b = round((balance - principal_pay))
    	print '''For month #2, minimum monthly pay: %r  Principal Paid: %s Remaining balance: %d ''' % (min_month_pay, principal_pay, remaining_b)

month_2('min_month_pay', 'principal_pay', 'remaining_b')
		
balance = int(raw_input('What is your starting outstanding balance? '))  

# start month 3

def month_3(min_month_pay, principal_pay, remaining_b):
	min_month_pay = round((balance * min_month_pay_rate))
	principal_pay = round((apr/12 * balance))
	remaining_b = round((balance - principal_pay))
    	print '''For month #3, minimum monthly pay: %r  Principal Paid: %s Remaining balance: %d ''' % (min_month_pay, principal_pay, remaining_b)


month_3('min_month_pay', 'principal_pay', 'remaining_b')

balance = int(raw_input('What is your starting outstanding balance? '))  

# start month 4

def month_4(min_month_pay, principal_pay, remaining_b):
	min_month_pay = round((balance * min_month_pay_rate))
	principal_pay = round((apr/12 * balance))
	remaining_b = round((balance - principal_pay))
    	print '''For month #4, minimum monthly pay: %r  Principal Paid: %s Remaining balance: %d ''' % (min_month_pay, principal_pay, remaining_b)

month_4('min_month_pay', 'principal_pay', 'remaining_b')

balance = int(raw_input('What is your starting outstanding balance? '))  

#start month 5

def month_5(min_month_pay, principal_pay, remaining_b):
	min_month_pay = round((balance * min_month_pay_rate))
	principal_pay = round((apr/12 * balance))
	remaining_b = round((balance - principal_pay))
    	print '''For month #5, minimum monthly pay: %r  Principal Paid: %s Remaining balance: %d ''' % (min_month_pay, principal_pay, remaining_b)

month_5('min_month_pay', 'principal_pay', 'remaining_b')

balance = int(raw_input('What is your starting outstanding balance? '))  

# Start month 6

def month_6(min_month_pay, principal_pay, remaining_b):
	min_month_pay = round((balance * min_month_pay_rate))
	principal_pay = round((apr/12 * balance))
	remaining_b = round((balance - principal_pay))
    	print '''For month #6, minimum monthly pay: %r  Principal Paid: %s Remaining balance: %d ''' % (min_month_pay, principal_pay, remaining_b)

month_6('min_month_pay', 'principal_pay', 'remaining_b')

balance = int(raw_input('What is your starting outstanding balance? '))  

# start month 7


def month_7(min_month_pay, principal_pay, remaining_b):
	min_month_pay = round((balance * min_month_pay_rate))
	principal_pay = round((apr/12 * balance))
	remaining_b = round((balance - principal_pay))
    	print '''minimum monthly pay: %r  Principal Paid: %s Remaining balance: %d ''' % (min_month_pay, principal_pay, remaining_b)



month_7('min_month_pay', 'principal_pay', 'remaining_b')

# start month 8

def month_8(min_month_pay, principal_pay, remaining_b):
	min_month_pay = round((balance * min_month_pay_rate))
	principal_pay = round((apr/12 * balance))
	remaining_b = round((balance - principal_pay))
    	print '''minimum monthly pay: %r  Principal Paid: %s Remaining balance: %d ''' % (min_month_pay, principal_pay, remaining_b)



month_8('min_month_pay', 'principal_pay', 'remaining_b')

# start month 9

def month_8(min_month_pay, principal_pay, remaining_b):
	min_month_pay = round((balance * min_month_pay_rate))
	principal_pay = round((apr/12 * balance))
	remaining_b = round((balance - principal_pay))
    	print '''minimum monthly pay: %r  Principal Paid: %s Remaining balance: %d ''' % (min_month_pay, principal_pay, remaining_b)



month_9('min_month_pay', 'principal_pay', 'remaining_b')


# start month 10

def month_10(min_month_pay, principal_pay, remaining_b):
	min_month_pay = round((balance * min_month_pay_rate))
	principal_pay = round((apr/12 * balance))
	remaining_b = round((balance - principal_pay))
    	print '''minimum monthly pay: %r  Principal Paid: %s Remaining balance: %d ''' % (min_month_pay, principal_pay, remaining_b)



month_10('min_month_pay', 'principal_pay', 'remaining_b')


# start month 11

def month_10(min_month_pay, principal_pay, remaining_b):
	min_month_pay = round((balance * min_month_pay_rate))
	principal_pay = round((apr/12 * balance))
	remaining_b = round((balance - principal_pay))
    	print '''minimum monthly pay: %r  Principal Paid: %s Remaining balance: %d ''' % (min_month_pay, principal_pay, remaining_b)



month_11('min_month_pay', 'principal_pay', 'remaining_b')



# start month 12

def month_10(min_month_pay, principal_pay, remaining_b):
	min_month_pay = round((balance * min_month_pay_rate))
	principal_pay = round((apr/12 * balance))
	remaining_b = round((balance - principal_pay))
    	print '''minimum monthly pay: %r  Principal Paid: %s Remaining balance: %d ''' % (min_month_pay, principal_pay, remaining_b)



month_12('min_month_pay', 'principal_pay', 'remaining_b')





















