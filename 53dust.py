# 53dust.py by Catrinel Berevoescu

import argparse
import mcb185
import math

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('fasta', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20,
	help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4,
	help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help ='soft mask')
arg = parser.parse_args()
print('dusting with', arg.fasta, arg.size, arg.entropy, arg.lower)

w = int(arg.size)
ent = float(arg.entropy)


for defline, seq in mcb185.read_fasta(arg.fasta):
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
		if mask[i] == True and arg.lower == False:
			masked_char.append('N')
		elif mask[i] == True and arg.lower == True:
			s = seq[i]
			masked_char.append(s.lower())
		else: masked_char.append(seq[i])
	masked_seq = ''.join(masked_char)
	print('>', defline)
	r = 60
	for i in range(0, len(masked_seq), r):
		print(masked_seq[i:i+r])