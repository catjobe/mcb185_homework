# 33birthday.py by Catrinel Berevoescu

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

finr1 = 0
for i in range(trials):
	ind_bday = []
	for i in range(people):
		personi = random.randint(0, days-1)
		ind_bday.append(personi)
		
	for j in ind_bday:
		reps = ind_bday.count(j)
		if reps > 1: 
			finr1 += 1
			break
	
print(finr1 / trials)