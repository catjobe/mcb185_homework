# 44skew.py by Catrinel Berevoescu

import sequence
import sys
import gzip
import mcb185

filepath = sys.argv[1]
w = sys.argv[2]
f = int(w)

def g_count(seq):
	return seq.count('G')
def c_count(seq):
	return seq.count('C')

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	gc_comp = sequence.gc_comp(seq[0:f])
	gc_skew = sequence.gc_skew(seq[0:f])
	g_count = g_count(seq[0:f])
	c_count = c_count(seq[0:f])
	print('0', gc_comp, gc_skew)
	for i in range(1, len(seq) - f + 1):
		if seq[i - 1] == 'C': 
			c_count -= 1
		if seq[i - 1] == 'G':
			g_count -= 1
		if seq[i + f - 1] == 'C':
			c_count += 1
		if seq[i + f - 1] == 'G':	
			g_count += 1
		gc_comp = (g_count + c_count) / f
		gc_skew = (g_count - c_count) / (g_count + c_count)
		print(i, gc_comp, gc_skew)