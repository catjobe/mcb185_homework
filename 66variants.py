# 66variants.py by Catrinel Berevoescu

import argparse
import gzip

parser = argparse.ArgumentParser(description='variant reporter')
parser.add_argument('gff', type=str, help='GFF file')
parser.add_argument('vcf', type=str, help='VCF file')
arg = parser.parse_args()

print(arg.gff, arg.vcf)

snps = {}
with gzip.open(arg.vcf, 'rt') as fp:
	for line in fp:
		rows = line.split()
		snp_chrom = rows[0]
		snp_loc = rows[1]
		snp_id = snp_chrom + '-' + snp_loc
		snps[snp_id] = []
	
with gzip.open(arg.gff, 'rt') as fp:
	for line in fp:
		rows = line.split()
		strand = rows[6]
		region = rows[2]
		chroms = rows[0]
		start = int(rows[3])
		end = int(rows[4])
		for snp in snps:
			snp_loc = int(snp.split('-')[1])
			if snp.split('-')[0] == chroms:
				if snp_loc >= start and snp_loc <= end and region not in snps[snp]:
					snps[snp].append(region)

for snp, regions in snps.items(): 
	if len(regions) > 0:
		print(snp.split('-')[0], snp.split('-')[1], sep = '\t', end = '\t')
		print(','.join(map(str, regions)))
	
