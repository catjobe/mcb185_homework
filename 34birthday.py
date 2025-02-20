# 34birthday.py by Catrinel Berevoescu

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

dup = 0

for i in range(trials):
	calendar = []
	for i in range(days):
		calendar.append(0)
		
	for i in range(people):
		birthday = random.randint(0, days-1)
		calendar[birthday] += 1
		if calendar[birthday] > 1: 
			dup += 1
			break
	
	del calendar

print(dup/trials)
	