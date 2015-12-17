iat=['-']
atc=[0]
tsb1=[]
tse1=[]
tsb2=[]
tse2=[]
st1=[]
st2=[]
tcwq=[]
tsb1t = 0
tse1t = 0
tsb2t = 0
tse2t = 0
stl1 = [(0,0.3,2),(0.3,0.58,3),(0.58,0.83,4),(0.83,1,5)]
stl2 = [(0,0.35,3),(0.35,0.60,4),(0.6,0.8,5),(0.8,1,6)]
iatl = [(0,0.25,1),(0.25,0.65,2),(0.65,0.85,3),(0.85,1,4)]

import random
def generateRandom(l):
	n = random.random()
	for i in l:
		if(i[0]<n and i[1]>n):
			return l[l.index(i)][2]
			
for i in range(25):
	if tse1t<=atc[-1]:
		tsb1.append(atc[-1])
		st = generateRandom(stl1)
		st1.append(st)
		tse1t = tsb1[-1]+st
		tse1.append(tse1t)
		tcwq.append(tsb1[-1]-atc[-1])
		
		tsb2.append("-")
		tse2.append("-")
		st2.append("-")
	
	else:
		if tse2t<=atc[-1]:
			tsb2.append(atc[-1])
			st = generateRandom(stl2)
			st2.append(st)
			tse2t = tsb2[-1]+st
			tse2.append(tse2t)
			tcwq.append(tsb2[-1]-atc[-1])
			
			tsb1.append("-")
			tse1.append("-")
			st1.append("-")
		
		else:
			# both able and baker are busy chaps
			# add it to the person with lower tse
			if tse1t<=tse2t:
				tsb1.append(tse1t)
				st = generateRandom(stl1)
				st1.append(st)
				tse1t = tsb1[-1]+st
				tse1.append(tse1t)
				tcwq.append(tsb1[-1]-atc[-1])
				
				tsb2.append("-")
				tse2.append("-")
				st2.append("-")
				
			else:
				tsb2.append(tse2t)
				st = generateRandom(stl2)
				st2.append(st)
				tse2t = tsb2[-1]+st
				tse2.append(tse2t)
				tcwq.append(tsb2[-1]-atc[-1])
				
				tsb1.append("-")
				tse1.append("-")
				st1.append("-")
	
	iat.append(generateRandom(iatl))
	atc.append(atc[-1]+iat[-1])
	
print "cust\tiat\tatc\tst1\tst2\ttsb1\ttse1\ttsb2\ttse2\ttcwq"
for i in range(25):
	print i,"\t",iat[i],"\t",atc[i],"\t",st1[i],"\t",st2[i],"\t",tsb1[i],"\t",tse1[i],"\t",tsb2[i],"\t",tse2[i],"\t",tcwq[i]