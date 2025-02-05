# 22fibonacci.py by Catrinel Berevoescu

v1 = 0
v2 = 1
print(v1)
print(v2)
for i in range(8):
	v3 = v1 + v2
	print(v3)
	v1 = v2
	v2 = v3