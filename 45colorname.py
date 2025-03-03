# 45colorname.py by Catrinel Berevoescu

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

ins = R, G, B

def dis(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d

with open(colorfile) as fp:
	mins = 768
	for line in fp:
		columns = line.split()
		# print(columns)
		out = columns[2]
		colors = columns[0]
		vals = out.split(',')
		Rout = int(vals[0])
		Gout = int(vals[1])
		Bout = int(vals[2])
		outs = Rout, Gout, Bout
		distance = dis(ins, outs)
		if distance < mins: 
			mins = distance
			color = colors
	print('Closest Official Color Name =', color)
fp.close()


