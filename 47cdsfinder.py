# 47cdsfinder.py by Catrinel Berevoescu

import sequence
import sys
import mcb185

prot = int(sys.argv[2])

def protein_finder(seq, direction):
	codon = 3 
	ids = 0
	
	for k in range(3):
		for i in range(k, len(seq) - codon + 1, codon):
			codon_seq = seq[i:i+3]
			protein = []
			
			if codon_seq == 'ATG':
				protein.append('M')
			
				for j in range(i+3, len(seq) - codon + 1, codon):
					codon_seq = seq[j:j+3]
				
					if codon_seq in ['TAA', 'TAG', 'TGA']:
						protein.append('*')
						break
					
					if codon_seq in ['TTT', 'TTC']: protein.append('F')
					elif codon_seq in ['GGT', 'GGC', 'GGA', 'GGG']: protein.append('G')
					elif codon_seq in ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG']: protein.append('L')
					elif codon_seq in ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC']: protein.append('S')
					elif codon_seq in ['TAT', 'TAC']: protein.append('Y')
					elif codon_seq in ['TGT', 'TGC']: protein.append('C')
					elif codon_seq in ['TGG']: protein.append('W')
					elif codon_seq in ['CCT', 'CCC', 'CCA', 'CCG']: protein.append('P')
					elif codon_seq in ['CAT', 'CAC']: protein.append('H')
					elif codon_seq in ['CAA', 'CAG']: protein.append('Q')
					elif codon_seq in ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']: protein.append('R')
					elif codon_seq in ['ATT', 'ATC', 'ATA']: protein.append('I')
					elif codon_seq in ['ACT', 'ACC', 'ACA', 'ACG']: protein.append('T')
					elif codon_seq in ['AAT', 'AAC']: protein.append('N')
					elif codon_seq in ['AAA', 'AAG']: protein.append('K')
					elif codon_seq in ['GTT', 'GTC', 'GTA', 'GTG']: protein.append('V')
					elif codon_seq in ['GCT', 'GCC', 'GCA', 'GCG']: protein.append('A')
					elif codon_seq in ['GAT', 'GAC']: protein.append('D')
					elif codon_seq in ['GAA', 'GAG']: protein.append('E')
				if '*' in protein:
					protein_seq = ''.join(protein)
					if len(protein_seq) > prot:
						print('>', name, '-', direction, '-', 'prot', '-', ids, sep='')
						print(protein_seq)
						ids += 1

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	codon = 3 
	ids = 0
	revseq = sequence.revcomp(seq)
	protein_finder(seq, 'normal')
	protein_finder(revseq, 'reverse')