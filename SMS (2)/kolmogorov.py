import random
nums = [random.random() for i in range(100)]
# nums = [1 for i in range(100)]
nums.sort()
dplus=[]
dmin=[]
for i in range(1,101):
	dplus.append((i/100.0)-nums[i-1])
	dmin.append(nums[i-1]-((i-1)/100.0))
	
d = max([max(dplus),max(dmin)])

print "accepted" if d<(1.36/(100**0.5)) else "rejected"