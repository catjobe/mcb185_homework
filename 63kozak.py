# 63kozak.py by Catrinel Berevoescu

import sys
import gzip

norm_ranges = []
comp_ranges = []
sequence = []
capture = False
rawseq = []
range_list = []

with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		f = line.split()
		
		if f[0] == 'CDS':
			ranges = f[1]
			ranged = ranges.rstrip().split('..')
			
			if 'complement' in ranged[0]:
				comp_range = ranged[1].replace(')', '')
				comp_ranges.append(comp_range)
			else: 
				norm_range = ranged[0]
				norm_ranges.append(norm_range)

		if 'ORIGIN' in line:
			capture = True
			continue
		
		if capture:
			if '//' in line: 
				break
			cleaned_lines = ''.join(f[1:])
			rawseq.append(cleaned_lines)
		
sequence = ''.join(rawseq)
		
a = [0] * 11
c = [0] * 11
g = [0] * 11
t = [0] * 11
		
for starts in norm_ranges:
	clean_start = int(starts.replace('join(', ''))

	kozak = sequence[clean_start-5:clean_start+6]
	for i in range(len(kozak)):
		if kozak[i] == 'a': a[i] += 1
		if kozak[i] == 'c': c[i] += 1
		if kozak[i] == 'g': g[i] += 1
		if kozak[i] == 't': t[i] += 1

a_r = [0] * 11
c_r = [0] * 11
g_r = [0] * 11
t_r = [0] * 11

new_comps = []
for start in comp_ranges:
    if ',' in start:
        new_starts = start.split(',')
        new_comps.append(new_starts[0].strip()) 
        new_comps.append(new_starts[1].strip()) 
    else:
        new_comps.append(start)

for start in new_comps:
	starts = int(start)
	kozak = sequence[starts-7:starts+4][::-1]
	for i in range(len(kozak)): # reverse complement
		if kozak[i] == 'a': t[i] += 1
		if kozak[i] == 'c': g[i] += 1
		if kozak[i] == 'g': c[i] += 1
		if kozak[i] == 't': a[i] += 1	
	
print('AC', 'IMTSU001', sep=' ')
print('XX')
print('ID', 'ECKOZ', sep=' ')
print('XX')
print('DE', 'blah')
print('PO', 'A', 'C', 'G', 'T', sep='\t')
for i in range(len(a)):
	print(i+1, a[i], c[i], g[i], t[i], sep='\t')
print('XX')
