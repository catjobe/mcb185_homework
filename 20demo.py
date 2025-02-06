# 20demo.py by Catrinel Berevoescu

import math
import random

# Tuples

print('Tuples')

t = 1, 2
print(t)
print(type(t))

person = 'Steve', 21, 57891.50
print(person)

def midpoint(x1, y1, x2, y2):
	x = (x1 + x2) / 2
	y = (y1 + y2) / 2
	return x, y

print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)
mx, my = midpoint(1, 2, 3, 4)
print(mx, my)

print(m[0], m[1])

# Iteration

print('Iteration')
	
# while

print('while')

i = 0
while True:
	i = i + 1
	print('hey', i)
	if i == 3: break	

i = 0
while i < 3:
	i = i + 1
	print('hey', i)
	
i = 0
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)

# for i in range()

print('for i in range()')

for i in range(1, 10, 3):
	print(i)
	
for i in range(0, 5):
	print(i)

for i in range(5):
	print(i)
	
for i in range(5): print(i)
for i in range(0, 5): print(i)
for i in range(0, 5, 1): print(i) # these all do the same thing

# for item in container

print('for item in container')

basket = 'milk', 'eggs', 'bread'
for thing in basket:
	print(thing)
	
for i in range(len(basket)): 
	print(basket[i])

# Nesting

print('Nesting')

for i in range(7):
	if i % 2 == 0: print(i, 'is even')
	else: print(i, 'is odd')

# Practice Problems

print('Practice Problems')

# A function that calculates the triangular number, the sum of numbers from 1 to n

def triangular(n):
	total = 0
	for i in range(1, n+1):
		total += i
	return total
print(triangular(4))

# A function that calculates the factorial of a number

def factorial(n):
	if n <= 1: return 1
	product = 1
	for i in range(1, n+1):
		product *= i
	return product
print(factorial(5))
print(factorial(4))

# A function that computes the Poisson probability of k events occurring with an expectation of n:n^k e^-n / k!

def poisson(n, k):
	return n**k * math.e**(-n) / factorial(k)
print(poisson(10, 2))

# A function that solves "n choose k": n! / k!(n - k)!

def n_choose_k(n, k):
	return factorial(n) / (factorial(k) * factorial(n-k))
print(n_choose_k(6, 2))

# A function that estimates Euler's number: e

e = 0
for n in range(20):
	e = e + 1 / factorial(n)
print(e)

def euler(limit):
	e = 0
	for n in range(limit):
		e = e + 1 / factorial(n)
	return e
print(euler(20))

# A function that determines if a number is prime

def is_prime(n):
	for i in range(2, n // 2):
		if n % i == 0: return False
	return True
print(is_prime(7)) # prime
print(is_prime(8)) # not prime

# A function that estimates Pi using the Nilakantha series

def pi_calc(rep):
	p = 3
	for i in range(1, 1+rep):
		n = 2 * i
		d = n * (n + 1) + (n + 2)
		if i % 2 == 0: p +=  4 / d
		else: p += 4 / d
	return p
print(pi_calc(5))	

# Random Numbers

print('Random Numbers')

for i in range(5):
	print(random.random())
	
for i in range(3): # inclusive end points
	print(random.randint(1, 6))

random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())

# More Practice

print('More Practice')

# Monty Pi-thon

print('Monty Pi-thon')

n = 0
total = 0
while n < 10: # so I can continue the practice
	rand_x = random.random()
	rand_y = random.random()
	dist = math.sqrt(rand_x**2 + rand_y**2)
	total += 1
	if dist <= 1:
		n += 1
	pi = 4 * (n / total)
	print(pi)
	
# D&D Stats

print('D&D Stats')

random.seed(None)

# 3D6: roll 3 six-sided dice

print('3D6')

threed6 = 0 
for i in range(3):
	d = random.randint(1, 6)
	threed6 += d
print(threed6)
 
n = 10000
for i in range(n):
	threed6 = 0
	for j in range(3):
		d = random.randint(1, 6)
		threed6 += d
	total += threed6
average = total / n
print(average)

# 3D6r1: roll 3 six-sided dice, but re-roll any 1s

print('3D6r1')	

threed6r1 = 0
for i in range(3):
	d = random.randint(1, 6)
	print(d)
	while d == 1:
		d = random.randint(1, 6)
		print(d)
	threed6r1 += d
print(threed6r1)

n = 10000
total = 0
for i in range(n):
	threed6r1 = 0
	for j in range(3):
		d = random.randint(1, 6)
		while d == 1:
			d = random.randint(1, 6)
		threed6r1 += d
	total += threed6r1
average = total / n
print(average)

# 3D6x2: roll pairs of six-sided 3 times, taking the maximum each time

print('3D6x2')

threed6x2 = 0
for i in range(3):
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	if d1 > d2: final = d1
	else: final = d2
	threed6x2 += final
print(threed6x2)

n = 10000
total = 0
for i in range(n):
	threed6x2 = 0
	for j in range(3):
		d1 = d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 > d2: final = d1
		else: final = d2
		threed6x2 += final
	total += threed6x2
average = total / n
print(average)

# 4D6d1: roll 4 six-sided dice, dropping the lowest die roll

print('4D6d1')

fourD6d1 = 0
for i in range(1):
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	d4 = random.randint(1, 6)
	if d1 < d2 and d1 < d3 and d1 < d4: final = d2 + d3 + d4
	elif d2 < d1 and d2 < d3 and d2 < d4: final = d1 + d3 + d4
	elif d3 < d1 and d3 < d2 and d3 < d4: final = d1 + d2 + d4
	else: final = d1 + d2 + d3
print(final)

# Assessment Examples

print('Assessment Examples')

# Fizzbuzz 2.0

for i in range(1, 101):
	if i % 3 == 0: print('Fizz')
	elif i % 5 == 0: print('Buzz')
	else: print(i)

# Pi estimate - Gregory-Leibniz series

minipi = 1
s = 1
while s < 20:
	n = 3 + (2 * (s - 1))
	s += 1 
	if s % 2 == 0:
		minipi += -(1 / n)
	else: minipi += 1 / n
	pi = 4 * minipi
	print(pi)

# Halflings Death Save

def max_roll(r1, r2):
	if r1 > r2: print(r1)
	return r2

def death_saves():
	success = 0
	failure = 0
	health = 0
	while success < 3 and failure < 3 and health == 0:
		roll1 = random.randint(1, 20)
		roll2 = random.randint(1, 20)
		roll = max_roll(roll1, roll2) 
		# print(roll)
		if roll == 1:
			failure += 2
		elif roll < 10:
			failure += 1
		elif roll < 20:
			success += 1
		else: health += 1
	# print(failure, success, health)
	if health == 1: 
		return 'revived'
	elif success >= 3: 
		return 'stable'
	else: 
		return 'dead'
# print(death_saves())

revived = 0
dead = 0
stable = 0
total = 1000
for i in range(total):
	status = death_saves()
	if status == 'dead': 
		dead += 1
	elif status == 'stable':
		stable += 1
	else:
		revived += 1
print('Revived Probability =', revived / total)
print('Stable Proability =', stable / total)
print('Death Probability =', dead / total)
	
# Pi estimates, refined

minipi = 1
s = 1
while pi < 3.1414 and pi > 3.1416 : 
	n = 3 + (2 * (s - 1))
	s += 1 
	if s % 2 == 0:
		minipi += -(1 / n)
	else: minipi += 1 / n
	pi = 4 * minipi
	print(pi)