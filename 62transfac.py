# 62transfac.py by Catrinel Berevoescu

import json
import sys
import gzip

pwms = []	
current_pwm = None

with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		names = line.split()
	
		if names[0] == 'ID': 
			if current_pwm:
				pwms.append(current_pwm)
			current_pwm = {'id': names[1], 'pwm': []}
			
		if line.startswith('0'):
			if pwms is not None:
				pwm = {
					'A': (names[1]), 
					'C': (names[2]),
					'G': (names[3]), 
					'T': (names[4])
				}
				current_pwm['pwm'].append(pwm)
				
		if names[0] == '//':
			if current_pwm:
				pwms.append(current_pwm)
				current_pwm = None

print(json.dumps(pwms, indent=4))