# 35scoringmatrix.py by Catrinel Berevoescu

import sys

alphabet = sys.argv[1]
matches = sys.argv[2]
mismatches = sys.argv[3]

alpha = list(alphabet)
print(alpha)

print(end='   ')
for a in alpha:
	print(a, end='  ')
print()

for a in alpha:
	print(a, end=' ')
	for b in alpha:
		if a == b: print(matches, end=' ')
		else: print(mismatches, end=' ')
	print()