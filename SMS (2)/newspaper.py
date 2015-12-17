#newspaper
gfp = [(0,0.35,"good"),(0.35,0.80,"fair"),(0.8,1,"poor")]
num = {0:[(0,0.03,40),(0.03,0.08,50),(0.08,0.23,60),(0.23,0.43,70),(0.43,0.78,80),(0.78,0.93,90),(0.93,1,100)],
1:[(0,0.1,40),(0.1,0.28,50),(0.28,0.68,60),(0.68,0.88,70),(0.88,0.96,80),(0.96,1,90),(1,1,100)],
2:[(0,0.44,40),(0.44,0.66,50),(0.66,0.82,60),(0.82,0.94,70),(0.94,1,80),(1,1,90),(1,1,100)]}

n = 70
tod=[]
dem=[]
inv=70*33
sales=[]
lfed=[]
rfs=[]
profit=[]

import random
def generateRandom(l):
	n = random.random()
	for i in l:
		if(i[0]<n and i[1]>n):
			return l.index(i)

for i in range(20):
	temp=generateRandom(gfp)
	tod.append(gfp[temp][2])
	dem.append(num[temp][generateRandom(num[temp])][2])
	lfed.append(0 if dem[-1]<=70 else 17*(dem[-1]-70))
	rfs.append(0 if dem[-1]>70 else 5*(dem[-1]-70))
	sales.append(70 * 50 if dem[-1]>70 else dem[-1]*50)
	profit.append((sales[-1]+rfs[-1]-lfed[-1]-inv)/100.0)

print profit, sum(profit)
	
