#(M,N) inventory
m = 11
n = 5
ltl = [(0,0.6,1),(0.6,0.9,2),(0.9,1,3)]
deml = [(0,0.1,0),(0.1,0.35,1),(0.35,0.7,2),(0.7,0.91,3),(0.91,1,4)]
beginv = [8]
endinv = []
dem = []
short = []
order = []
lt = []
ltt = -1

import random
def generateRandom(l):
	n = random.random()
	for i in l:
		if(i[0]<n and i[1]>n):
			return l[l.index(i)][2]


for i in range(20+1):
		
	dem.append(generateRandom(deml))
	endinv.append(0 if dem[-1]>=beginv[-1] else (beginv[-1]-dem[-1]))
	if dem[-1]>beginv[-1]:
		short.append(short[-1]+dem[-1]-beginv[-1])
	else:
		short.append(0)
		
	if(i%n == 0):
		ltt = generateRandom(ltl)
		print i,short[-1]-endinv[-1]+m
		order.append(short[-1]-endinv[-1]+m)
	
	if(ltt == 0):
		beginv.append(endinv[-1]+order[-1]-short[-1])
	if(not ltt == 0):
		beginv.append(endinv[-1])
	if(ltt>=0):
		lt.append(ltt)
	else:
		lt.append("-")
	ltt-=1
		
print "day\tcycle\tbegin\tdem\tend\tshort\torder\tlt"
cycle = 0
p=0
print order
for i in range(20+1):
	print i, "\t", cycle,"\t", beginv[i],"\t", dem[i],"\t", endinv[i],"\t", short[i],"\t", 
	if(i%n == 0):
		print order[p],"\t",
		cycle+=1
	else:
		print "-","\t",
	if(i%n==n-1):
		p+=1
	
	print lt[i]