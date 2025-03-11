# 54missingkmers.py by Catrinel Berevoescu

import sys
import mcb185
import itertools

	
def kmer_counter(seq):
	for i in range(len(seq) - k + 1):
		kmer = seq[i:i+k]
		if kmer not in kcount: kcount[kmer] = 0
		kcount[kmer] += 1

ghost_kmer = 0
k = 1

while ghost_kmer == 0:
	kcount = {}
	
	for defline, seq in mcb185.read_fasta(sys.argv[1]):
		strand1 = seq
		strand2 = mcb185.anti_seq(seq)
		kmer_counter(strand1)
		kmer_counter(strand2)
	
	for nts in itertools.product('ACGT', repeat = k):
		kmer = ''.join(nts)
		if kmer not in kcount: 
			print(kmer, 0)
			ghost_kmer += 1
	k += 1