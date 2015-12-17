import random
nums = [random.random() for i in range(100)]

k = 10 # number of classes
l = [(max(nums)*i/float(k),max(nums)*(i+1)/float(k)) for i in range(k)]
freq=[0]*k
for num in nums:
	for i in l:
		if(i[0]<num and i[1]>num):
			freq[l.index(i)] += 1
			
E = [len(nums)/float(k)] * k
xsquare = sum([(((freq[i]-E[i])**2)/E[i]) for i in range(k)])
print xsquare