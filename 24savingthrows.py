# 24savingthrows.py by Catrinel Berevoescu

import random

def max_roll(r1, r2): 
	if r1 > r2: return r1
	return r2

def min_roll(r1, r2):
	if r1 > r2: return r2
	return r1

def saving_throw(dc, event):
	print('DC =', dc, ',', 'Event =', event)
	if event == 'none':
		roll = random.randint(1, 20)
		print('roll =', roll)
		if roll >= dc: return 'success'
		return 'fail'
	else:
		roll1 = random.randint(1, 20)
		print('roll1 =', roll1)
		roll2 = random.randint(1, 20)
		print('roll2 =', roll2)
		if event == 'advantage':
			roll = max_roll(roll1, roll2)
			if roll >= dc: return 'success'
			return 'fail'
		else:
			roll = min_roll(roll1, roll2)
			if roll >= dc: return 'success'
			return 'fail'
print(saving_throw(15, 'advantage'))
print(saving_throw(5, 'disadvantage'))
print(saving_throw(10, 'none'))