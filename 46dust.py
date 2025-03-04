# 46dust.py by Catrinel Berevoescu

import sys
import mcb185
import math

w = int(sys.argv[2])
ent = float(sys.argv[3])

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	mask = [False] * len(seq)
	for i in range(1, len(seq) - w + 1):
		h = 0
		s = seq[i:i+w]
		a_p = s.count('A') / w
		c_p = s.count('C') / w
		g_p = s.count('G') / w
		t_p = s.count('T') / w
		p = a_p, c_p, g_p, t_p
		for nt_p in p:
			if nt_p == 0: h -= 0
			else: h -= nt_p * math.log2(nt_p)
		if h < ent:
			for j in range(i, i+w):
				mask[j] = True
	masked_char = []
	for i in range(len(seq)):
		if mask[i] == True:
			masked_char.append('N')
		else: masked_char.append(seq[i])
	masked_seq = ''.join(masked_char)
	print('>', defline)
	r = 60
	for i in range(0, len(masked_seq), r):
		print(masked_seq[i:i+r])