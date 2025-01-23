# 12phred.py by Catrinel Berevoescu

import math

def char_to_prob(c): return 1 / (10 ** ((ord(c) - 33) / 10))
print(char_to_prob('I'))
print(char_to_prob('A'))

def prob_to_char(p): 
	return chr(int(math.log10(1 / p) * 10) + 33)
print(prob_to_char(0.001))
print(prob_to_char(0.0001))
