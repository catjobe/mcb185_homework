# 32stats.py by Catrinel Berevoescu

import sys
import math

nums = []
nums = sys.argv[1:]

# The number of values in nums

length = len(nums) 
print('Number of values =', length)

# The minimum and maximum values in nums

mins = float(nums[0])
maxs = float(nums[0])
for num in nums:
	num = float(num)
	if num < mins: mins = num
	if num > maxs: maxs = num
print('Min =', mins, 'Max =', maxs)
	
# The mean and standard deviation

def means(nums):
	total = 0
	for num in nums: 
		intn = float(num)
		total += intn
	return total / len(nums)
print('Mean =', means(nums))

tot = 0
means = means(nums)
sums = 0
for num in nums:
	intn = float(num)
	parts = (intn - means) ** 2
	sums += parts
sd = math.sqrt(sums / (length - 1))
print('Standard Deviation =', sd)

# Median value

nums = list(map(float, nums))
nums.sort()
half = int(length/2)
if int(length) % 2 == 0: 
	rup = int(half)
	rdo = int(half - 1)
	up = int(nums[rup])
	do = int(nums[rdo])
	median = (up + do) / 2
	print('Median =', median)
else: 
	median = nums[half]
	print('Median =', median)

