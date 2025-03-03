# 40cdslength.py by Catrinel Berevoescu

import gzip
import sys

with gzip.open(sys.argv[1], 'rt') as filepath:
	for line in filepath:
		if line[0] != '#':
			words = line.split()
			if words[2] == 'CDS':
				beg = int(words[3])
				end = int(words[4])
				print(end - beg + 1)