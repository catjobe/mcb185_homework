# 48transmembrane.py by Catrinel Berevoescu

import sequence
import sys
import mcb185

def hydro(seq, l, ht):
	for i in range(0, len(seq) - l + 1):
		s = seq[i:i+l]
		score = 0
		if 'P' in s:
			continue
		for aa in s:
			if aa == 'A': score += 1.80
			elif aa == 'C': score += 2.50
			elif aa == 'D': score -= 3.50
			elif aa == 'E': score -= 3.50
			elif aa == 'F': score += 2.80
			elif aa == 'G': score -= 0.40
			elif aa == 'H': score -= 3.20
			elif aa == 'I': score += 4.50
			elif aa == 'K': score -= 3.90
			elif aa == 'L': score += 3.80
			elif aa == 'M': score += 1.90
			elif aa == 'N': score -= 3.50
			elif aa == 'Q': score -= 3.50
			elif aa == 'R': score -= 4.50
			elif aa == 'S': score -= 0.80
			elif aa == 'T': score -= 0.70
			elif aa == 'V': score += 4.20
			elif aa == 'W': score -= 0.90
			elif aa == 'Y': score -= 1.30
		kd = score / l
		if kd >= ht: 
			return True
	return False

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if hydro(seq[:30], 8, 2.5) and hydro(seq[30:], 11, 2.0): print(defline)
	
		