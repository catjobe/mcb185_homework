# 30demo.py by Catrinel Berevoescu

import math

# Strings

print('Strings')

s = 'hello world'
print(s)

s1 = 'hey "dude"' # one way to put a quote inside a string is to put single quotes inside double quotes
s2 = "don't tell me what to do" # can use single, double, and triple quotes as string delimiters
print(s1, s2)

print('hey "dude" don\'t tell me what to do') # another strategy is to backslash the quote; backslashes = special characters

# Method Syntax

print('Method Syntax')

print(s.upper()) # gives uppercase version of s
print(s)

print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i')) # this converts substring 'o' in case 1 with nothing

# String Formatting

print('String Formatting')

print(f'{math.pi}')
print(f'{math.pi:.3f}') # 3 fixed digits after the decimal (approximation)
print(f'{1e6 * math.pi:3}') # exponent notation
print(f'{"hello world":>20}') # right justify with space filler
print(f'{"hello world":.>20}') # right justify with dot filler
print(f'{20:<10} {10}') # left justify

print('{} {:.3f}'.format('str.format', math.pi)) # str.format() style
print('%s %.3f' % ('printf', math.pi)) # printf-style; similar to str.format(), what is on right is filled in with whats on the left

# Indexes

print('Indexes')

seq = 'GAATTC'
print(seq[0], seq[1]) # where seq[0] is the first letter of the sequence and seq[1] is the second

print(seq[-1]) # if indexes are negative, they count backwards from the right; seq[-1] is the last character of the string

for nt in seq:
	print(nt, end='')
print()

for i in range(len(seq)): # iterates through letters by indices
	print(i, seq[i])

# Slices

print('Slices')

s = 'ABCDEFGHIJ'
print(s[0:5]) # similarly to range(), takes initial position and end-before limit

print(s[0:8:2]) # can have a step size, if omitted step size is 1

print(s[0:5], s[:5])  # can omit initial value (0)
print(s[5:len(s)], s[5:]) # can omit final value (length of string)

print(s, s[::], s[::1], s[::-1]) # the first three will output the same thing, last reverse order

dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
	codon = dna[i:i+3]
	print(i, codon)
	
# Tuples

print('Tuples')

tax = ('Homo', 'sapiens', 9606)
print(tax) # comma separated values in parentheses

print(tax[0]) # linear container of values, can be indexed and sliced with same syntax as strings
print(tax[::-1]) # slice 

# enumerate() and zip()

print('enumerate() and zip()')

# enumerate()

print('enumerate()')

nts = 'ACGT'
for i in range(len(nts)): # have both indices and values with range()
	print(i, nts[i])
	
for i, nt in enumerate(nts): # neater way of doing the same thing
	print(i, nt)
	
# zip()

print('zip()')

names = ('adenine', 'cytosine', 'guanine', 'thymine') # can use range() to simultaneously index separate containers
for i in range(len(names)):
	print(nts[i], names[i])
	
for nt, name in zip(nts, names): # tidier way of doing the same thing
	print(nt, name)
	
for i, (nt, name) in enumerate(zip(nts, names)): # can enumerate the zip
	print(i, nt, name)
	
# Lists

nts = ['A', 'T', 'C'] # similar to tuples but square brackets and content mutable
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C') # element C added to the end
print(nts)

last = nts.pop() # remove elements at the end
print(last)

nts.sort() 
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts # a new variable to an existing list is just another name for the same list, not a copy
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

nucleotides_copy = nucleotides.copy() # use list.copy() to make a "shallow" copy
print(nucleotides_copy)

# list()

print('list()')

items = list() # empty list
print(items) 
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)

alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph) # converts string into a list of letters
print(aas)

# split() and join()

print('split() and join()')

text = 'good day     to you' # delimiter is any number of spaces
words = text.split() # splits strings into lists of strings
print(words)

line = '1.41,2.72,3.14' 
print(line.split(',')) # if delimiter is ,

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

# Searching

print('Searching')

if 'A' in alph: print('yay') # use in to search for A in alph
if 'a' in alph: print('no')

print('index G?', alph.index('G')) # index() returns the index of the first element found
# print('index Z?', alph.index('Z')) if no matching item, error

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z')) # find() returns -1 if it can't be found; only works for strings

# Practice Problems

print('Practice Problems')

# Function that returns minimum value of a list

alpha = ['A', 'B', 'C', 'D']

def minimum(v):
	min = v[0]
	for v in v[1:]:
		if v < min: min = v
	return min

print(minimum(alpha))

# A function that returns minimum and maximum values of a list

def min_max(v):
	min = v[0]
	max = v[0]
	for v in v[1:]:
		if v < min: min = v
		if v > max: max = v
	return min, max

print(min_max(alpha))

# A function that returns the mean of the values

numbs = [1, 2, 3, 4]

def mean_value(v):
	total = 0
	for value in v: total += value
	return total / len(v)

print(mean_value(numbs))

# A function that computes entropy of a probability distribution

probs = [0.5, 0.5, 0]

def entropy(p):
	h = 0
	for probs in p:
		if probs == 0: h -= 0
		else: h -= probs * math.log2(probs)
	return h

print(entropy(probs))

# A function that computes Kullback-Leibler distance between two sets of probability distributions

P = [0.5, 0.5]
Q = [0.75, 0.25]

def kld(P, Q):
	d = 0
	for p1, p2 in zip(P, Q):
		if p1 == 0 and p2 == 0: d += 0
		else: d += p1 + math.log2(p1 / p2)
	return d
print(kld(P, Q))

# Command Line Data

print('Command Line Data')

# sys.argv

print('sys.argv')

import sys
print(sys.argv)

# Converting Types

print('Converting Types')

i = int('42')
x = float('0.61803')
print(i * x)

# x = float('hello') this would give an error; if run into error use sys.exit() for custom message

# Pairwise Comparison

print('Pairwise Comparison')

list = ('a', 'b', 'c', 'd')

# All Combinations

print('All Combinations')

for i in range(0, len(list)):
	ival = list[i]
	for j in range(0, len(list)): 
		jval = list[j]
		print(ival, jval)
		
# Half-Matrix with Diagonal

print('Half-Matrix with Diagonal')

for i in range(0, len(list)):
	ival = list[i]
	for j in range(i, len(list)):
		jval = list[j]
		print(ival, jval)
		
# Half-Matrix without Diagonal

print('Half-Matrix without Diagonal')
		
for i in range(0, len(list)):
	ival = list[i]
	for j in range(i+1, len(list)):
		jval = list[j]
		print(ival, jval)
		
# Assessment Examples

# 1. Figuring out what will be printed

# print('-'.join(list('ABCDE'))[3:6]) # 1. the'-'.join(list('ABCDE')) A-B-C-D-E 2. the index [3:6] results in -C-

# 2. N50 Calculation

print('N50')

nums = [2, 3, 4, 10, 6, 7, 8, 9, 5]

nums.sort()
print('Numbers = ', nums)
tot_num = 0
for num in nums:
	tot_num += num
half = tot_num / 2
h = 0
for num in nums[::-1]:
	h += num
	if h >= half:
		print('N50 =', num)
		break
	

# 3. Given a nucleotide sequence such as ATGCTGTAA, create an output that shows the position, frame, and codon separated by tabs

print('Nt sequence')

nt_seq = ('ATGCTGTAATAA')

for i in range(len(nt_seq) - 2):
	codon = nt_seq[i:i+3]
	print(i+1, (i % 3) + 1, codon, sep = '\t')
		