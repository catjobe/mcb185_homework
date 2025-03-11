# 50demo.py by Catrinel Berevoescu

import random
import time

# Sets

print('Sets')

s = {'A', 'B', 'C'}
print(s)

s.add('T')
print(s)

s.add('A')
print(s)

# print(s[2]) generates an error

def random_names(n, k):
	klist = list()
	kset = set()
	for _ in range(n):
		kmer = ''.join(random.choices('ACGT', k=k))
		klist.append(kmer)
		kset.add(kmer)
	return klist, kset

for size in range(1000, 1000, 1000):
	
	list1, set1 = random_names(size, 10)
	list2, set2 = random_names(size, 10)
	
	t0 = time.time()
	for name1 in list1:
		if name1 in list2: pass
	t1 = time.time()
	list_time = t1 - t0
	
	t0 = time.time()
	for name1 in list1:
		if name1 in set2: pass
	t1: time.time()
	set_time = t1 - t0
	
# Dictionaries

print()
print('Dictionaries')

d = {} 
d = dict() # two ways to create empty dictionaries

d = {'dog': 'woof', 'cat': 'meow'}
print(d)

print(d['cat']) # access items with square brackets

d['pig'] = 'oink' # add new items to dictionary
print(d)

d['cat'] = 'mew' # change the value of an item
print(d)

del d['cat'] # delete an item
print(d)

# print(d['rat']) get an error if try to access a key that doesn't exist

if 'dog' in d: print(d['dog'])

# Iteration

print()
print('Iteration')

for key in d: print(f'{key} says {d[key]}')
for k, v in d.items(): print(k, 'says', v) # most common way
for thing in d.items(): print(thing[0], thing[1])
print(d.keys(), d.values(), list(d.values()))

# Lookup Tables

print()
print('Lookup Tables')

kdtables = {'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):
	kd = 0
	for aa in seq: kd += kdtables[aa]
	return kd/len(seq)

seq = 'VGEWPP'
print(kd_dict(seq))

# Composition, again

print()
print('Composition, again')

count = {}
for nt in seq:
	if nt not in count: count[nt] = 0
	count[nt] += 1
print(count)

# Sorting

print()
print('Sorting')

for k in sorted(count): print(k, count[k])

for k, v in sorted(count.items(), key=lambda item: item[1]):
	print(k, v)
	
def by_value(tuple):
	return tuple[1]
	
for k, v in sorted(count.items(), key=by_value):
	print(k, v)
	
# Kmers

print()
print('Kmers')

import itertools
for nts in itertools.product('ACGT', repeat=2):
	print(nts)
	
# Argparse

print()
print('Argparse')

# Named Arguments

print('first', 'second') # positional only
print('first', 'second', sep='\t', end='\n') # named
print('first', 'second', end='\n', sep='\n') # named, different order