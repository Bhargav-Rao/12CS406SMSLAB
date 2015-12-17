import random, math
nums = [0.661,5.124,13.509,15.512,2.731,2.42,6.255,6.892,12.413,4.37,4.91,15.033,5.745,2.758,6.892,2.984,27.969,13.243,2.169,0.377,8.989,22.091,0.651,17.602,16.713,10.613,12.107,12.711,0.921,9.063,12.801,1.543,0.965,6.675,5.692,3.827,4.636,3.411,1.9,1.875,20.249,3.624,25.146,11.209,6.636,10.244,7.093,7.897,0.315,0.79,]

k = 8 # number of classes
lamb = 1/float(k)
a = [-(1/float(lamb) * math.log(1 - (i*(lamb)))) for i in range(k)]
# for i in range(k):
	# print i,math.log(1 - (i*(lam)))
print a
	
a.append(99999999999)
l = [(a[i],a[i+1]) for i in range(k)]
freq=[0]*k
for num in nums:
	for i in l:
		if(i[0]<num and i[1]>num):
			freq[l.index(i)] += 1
			
E = [len(nums)/float(k)] * k
xsquare = sum([(((freq[i]-E[i])**2)/E[i]) for i in range(k)])
print xsquare