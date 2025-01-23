# 11oligo.py by Catrinel Berevoescu

import math

def tm(a, c, t, g):
	total = a + c + t + g
	if total <= 13: return (a + t) * 2 + (g + c) * 4
	else: return 64.9 + 41 * (g + c - 16.4) / total

print(tm(1, 2, 3, 4)) # oligo <= 13 nt
print(tm(2, 4, 3, 4)) # oligo = 13 nt
print(tm(5, 7, 3, 4)) # oligo > 13 nt
