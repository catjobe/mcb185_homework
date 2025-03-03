# test_sequence.py by Catrinel Berevoescu

import sequence

print(sequence.transcribe('ACGT'))
print(sequence.revcomp('AAAACGT'))
print(sequence.translate('ATGCCCTAA')) # returns MX*

s = 'ACGTGGGGGGCATATG'
print(sequence.gc_comp(s))
print(sequence.gc_skew(s), sequence.gc_skew(sequence.revcomp(s)))