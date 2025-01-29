# 10_test.py by Catrinel Berevoescu

# A function that returns the maximum of 4 numbers

def max4(a, b, c, d):
	if a >= b and a >= c and a >= d: 
		return a
	elif b >= a and b >= c and b >= d: 
		return b
	elif c >= a and c >= b and c >= d: 
		return c
	else: 
		return d
	
print(max4(1, 2, 3, 4))
print(max4(1, 3, 3, 3))

# A function that determines if a number is a valid probability

def valid_prob(p):
	if p >= 0 and p <= 1: 
		return 'is a valid probability'
	else: 
		return 'is not a valid probability'
	
print(valid_prob(0.5))
print(valid_prob(1.1))

# A function that reports the "reading frame" of a position

def reading_frame(nt):
	if nt % 3 == 0: 
		return '3'
	elif nt % 3 == 1: 
		return '1'
	else: 
		return '2'
	
print(reading_frame(5))	
print(reading_frame(3))	
print(reading_frame(4))
print(reading_frame(12))