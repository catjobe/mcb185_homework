# 47cdsfinder.py by Catrinel Berevoescu

import sys
import mcb185
import sequence

win = float(sys.argv[2])

def protein_finder(seq, w, label):
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
			if len(protein) > w and '-' not in protein: 
				print('>', name, '-', 'prot' , '-', label, '-', ids, sep='')
				print(protein, '*', sep='')
				ids += 1


for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	revseq = sequence.revcomp(seq)
	protein_finder(seq, win, 'nor')
	protein_finder(revseq, win, 'rev')	


