# 25deathsaves.py by Catrinel Berevoescu

import random

def death_saves():
	success = 0
	failure = 0
	health = 0
	while success < 3 and failure < 3 and health == 0:
		roll = random.randint(1, 20)
		if roll == 1:
			failure += 2
		elif roll < 10:
			failure += 1
		elif roll < 20:
			success += 1
		else: health += 1
	if health == 1: 
		return 'revived'
	elif success >= 3: 
		return 'stable'
	else: 
		return 'dead'
print('Death Saves Simulation =', death_saves())

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