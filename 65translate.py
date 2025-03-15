# 65translate.py by Catrinel Berevoescu

import argparse
import mcb185

parser = argparse.ArgumentParser(description='mRNA translator.')
parser.add_argument('file', type=str, help='fasta file of mRNAs')
parser.add_argument('-m', '--min', type=int, default=100,
    help='minimum protein lengh [%(default)i]')
parser.add_argument('-a', '--anti', action='store_true', help='also examine the anti-parallel strand')
arg = parser.parse_args()

print(arg.file, arg.min, arg.anti)

def protein_finder(seq, length, label):
	for i in range(3):
		ids = 0
		rawp = mcb185.translate(seq[i:])
		rawl = list(rawp)
		if rawp[len(rawp) - 1] != '*': rawl.append('-')
		rawl_n = ''.join(rawl)
		orfs = rawl_n.split('*')
		for orf in orfs:
			if 'M' not in orf: continue
			idx = orf.index('M')
			protein = orf[idx:]
			if len(protein) > length and '-' not in protein: 
				print('>', defline, sep='')
				r = 60
				for i in range(0, len(protein), 60):
					print(protein[i:i+r], sep='')
				ids += 1

for defline, seq in mcb185.read_fasta(arg.file):
	defwords = defline.split()
	name = defwords[0]
	if arg.anti:
		anti_seq = mcb185.anti_seq(seq)
		protein_finder(anti_seq, arg.min, defline)
		protein_finder(seq, arg.min, defline)
	else: protein_finder(seq, arg.min, defline)
