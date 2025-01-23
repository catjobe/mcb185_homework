# 10demo.py by Catrinel Berevoescu

import math
import random

print('hello, again') # greeting

"""
This is a
multi-line
comment
"""

print(1.5e-2)

# testing math operators

print('testing math operators')

print(5 + 10) # addition
print(10 - 15) # subtraction
print(5 * 5) # multiplication
print(5 / 2) # division
print(5 ** 2) # exponentiation
print(5 // 2) # integer division
print(5 % 2) # remainder
print((5 * (2 + 5)) / 3) # precedence

# testing math functions

print('testing math functions')

print(abs(-5)) # absolute value
print(pow(5,2)) # exponents
print(round(5.2309023, ndigits = 3)) # rounding
print(math.floor(5.5)) # rounding 5.5 down
print(math.log10(100)) # log 10 of 100

# variables example

print('variables example')

a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print(c)

print(type(a), type(b), type(c), sep=',', end='!\n') # identifying type of variable c

# writing a function

print('writing a function')

def pythagoras(a, b):
	c = math.sqrt(a**2 + b**2)
	return c

hyp = pythagoras(3,4)
print(hyp)

def pythagoras(a, b): # the simplified version
	return(math.sqrt(a**2 + b**2))
print(pythagoras (a, b))

# practice

print('practice')

def circle_area(r): return math.pi * r**2 # function for calculating the area of a circle
print(circle_area(3))

def rectangle_area(w, h): return w * h # function for calculating the area of a rectangle
print(rectangle_area(5, 2))

def triangle_area(w, h): return rectangle_area(w, h) / 2 # function for calculating the area of a triangle
print(triangle_area(5, 2))

def what_farenheit(c): return 4.5 * c + 32 # calculating farenheit from celsius
print(what_farenheit(0))

def what_celsius(f): return (f - 32) * (5 / 9) # calculating celsius from farenheit
print (what_celsius(32))

def what_mph(k): return k / 1.60934 # calculating mph from kph
print (what_mph(30))

def what_kph(k): return k * 1.6093 # calculating kph from mph
print (what_kph(15))

def dna_conc(o): return o * 50 # calculating DNA concentration from OD260
print(dna_conc(0.1))

def arithmetic_mean(x, y, z): return (x + y + z) / 3 # function for calculating the arithmetic mean
print(arithmetic_mean(1, 2, 3))

def geometric_mean(a, b, c): return ((a * b * c) ** (1 / 3)) # function for calculating the geometric mean
print(geometric_mean(1, 2, 3))

def harmonic_mean(d, e, f): return 3 / ((1 / d) + (1 / e) + (1 / f)) # function for calculating the harmonic mean
print(harmonic_mean(1, 2, 3))

def distance_calc(a, b, c, d): return math.sqrt(((a - c) ** 2) + ((b - d) ** 2))
print(distance_calc(0, 0, 3, 4))

# strings

print('strings practice')

s = 'hello world'
print(s, type(s))

# conditions - if, boolean, 

print('conditions practice')

# if

a = 2
b = 2
if a == b:
	print('a equals b')
	print(a, b)

if a == b:
	print('a equals b')
print(a, b) # second statement is after the block; the program will always report a and b

def is_even(x):
	if x % 2 == 0: return True
	return False
print(is_even(2))
print(is_even(3))

# boolean

c = a == b
print(c)
print(type(c))

# if-elif-else

if a < b: # only one if can exist
	print('a < b') 
elif a > b: # any number of elifs can exist
	print('a > b')
else: # there is only one else
	print('a == b')

if   a < b:	print('a < b')
elif a > b:	print('a > b')
else:	    print('a == b') #aligning these one-liners horizontally works

# chaining

a = 1
b = 10
if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

# Floating Point Warning

a = 0.3
b = 0.1 * 3
if a < b: print('a < b')
elif a > b: print('a > b')
else: print('a == b') # never test equality with floating point numbers

print(abs(a - b)) # 5.551115123125783e-17
if abs(a-b) < 1e-9: print('close enough') # how to manually get around the issue above

if math.isclose(a, b): print('close enough')

# string comparison

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a') # lowercase letters have higher ASCII values than uppercase letters

# mismatched type error

a = 1
s = 'G'
# if a < s: print('a < s') makes no sense to compare variables of different types

# none type

print('none type practice')

def silly(m, x, b):
	y = m * x + b
print(silly(2, 3, 4)) # no return in the function, so will get a value of None

# more practice

print('more practice')

def is_integer(i): return i % 1 == 0 # function that determines if a number is an integer
print(is_integer(5))

def valid_probability(p): # function that determines if value is a valid probability
	if p <= 1 and p >= 0: return True
	elif p < 0 or p > 1: return False
print(valid_probability(0.5)) 
print(valid_probability(1.5))
print(valid_probability(-0.5))

def dna_mw(n): # function that returns the molecular weight of DNA letter, else None
	if n == 'A': return '135.13 g/mol'
	elif n == 'T': return '126.1133 g/mol'
	elif n == 'C': return '111.1 g/mol'
	elif n == 'G': return '151.13 g/mol'
	else: return None
print(dna_mw('A'))
print(dna_mw('F'))

def dna_complement(n): # function that returns complement of DNA letter, else None
	if n == 'A': return 'T'
	elif n == 'T': return 'A'
	elif n == 'C': return 'G'
	elif n == 'G': return 'C'
	else:
		return None
print(dna_complement('T'))
print(dna_complement('Y'))

# even more practice

print('even more practice')

def max_finder(x, y, z): # finds the max of 3 numbers
	if x > y and x > z: return x
	elif y > x and y > z: return y
	else: return z
print(max_finder(1, 2, 3))

def sensitivity_calculator(tp, fn): return tp / (tp + fn)
print(sensitivity_calculator(15, 10))

def specificity_calculator(tn, fp): return tn / (tn + fp)
print(specificity_calculator(20, 5))

def f1_score(tp, fp, fn): return tp / (tp + 0.5 * (fp + fn))
print(f1_score(50, 5, 5))

print('shannon entropy')

def shannon_entropy(a, c, t, g): 
	total = a + c + g + t
	if a == 0: a = 0
	else: a = a / (total) * math.log2(a / (total))
	if c == 0: c = 0
	else: c = c / (total) * math.log2(c / (total))
	if t == 0: t = 0
	else: t = t / (total) * math.log2(t / (total))
	if g == 0: g = 0
	else: g = g / (total) * math.log2(g / (total))
	return -1 * (a + c + t + g)
print(shannon_entropy(50, 50, 50, 50))
print(shannon_entropy(0, 50, 50, 50))
print(shannon_entropy(0, 0, 50, 50))
