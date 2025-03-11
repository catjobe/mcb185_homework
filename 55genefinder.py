# 55genefinder.py by Catrinel Berevoescu

import sequence
import sys
import mcb185

orf_length = int(sys.argv[2])

def protein_finder(seq, defline, min_orf=100, strand='+'):
	for frame in range(3):
		i = frame
		while i < len(seq) - min_orf + 1:
			codon = seq[i:i+3] 
			if codon != 'ATG': 
				i += 3
				continue
			start = i
			stop = None
			for j in range(i+3, len(seq) - 2, 3):
				codon2 = seq[j:j+3]
				if codon2 in ['TAA', 'TAG', 'TGA']:
					stop = j + 3
					break
			if stop is None: 
				i += 3
				continue 
			i = stop + 1
			if stop - start >= (min_orf * 3 + 3): 
				if strand == '+':
					print(defline, start, stop, strand)
				else: 
					print(defline, len(seq) - stop, len(seq) - start, strand)

						
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	revseq = sequence.revcomp(seq)
	protein_finder(seq, name, min_orf=orf_length)
	protein_finder(revseq, name, strand='-', min_orf=orf_length)
