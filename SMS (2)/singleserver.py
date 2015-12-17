stl = [(0,0.1),(0.1,0.3),(0.3,0.6),(0.6,0.85),(0.85,0.95),(0.95,1)]
at = [(0.125 * 0,0.125 * 1),(0.125 * 1,0.125 * 2),(0.125 * 2,0.125 * 3),(0.125 * 3,0.125 * 4),(0.125 * 4,0.125 * 5),(0.125 * 5,0.125 * 6),(0.125 * 6,0.125 * 7),(0.125 * 7,0.125 * 8)]
import random
def generateRandom(l):
	n = random.random()
	for i in l:
		if(i[0]<n and i[1]>n):
			return l.index(i)+1
	
iat=['-']
atc=[0]
st=[]
tsb=[0]
tse=[]
tcwq=[]
tcss=[]
its=[0]

for i in range(20):
	# print tsb
	st.append(generateRandom(stl))
	tse.append(tsb[i]+st[i])
	tcwq.append(tsb[i]-atc[i])
	tcss.append((tse[i]-atc[i]))
	if i>0:
		# print i, len(tsb),tsb[i]
		# print tsb[i]-tsb[i-1]
		its.append(tsb[i]-tsb[i-1])
	iat.append(generateRandom(at))
	atc.append(iat[-1]+atc[-1])
	if(atc[-1]>=tse[-1]):
		tsb.append(atc[-1])
	else:
		tsb.append(tse[-1])

print 'iat \t atc \t st \t tsb \t tse \t tcwq \t tcss\t its'
for i in range(20):
	print iat[i],"\t",atc[i],"\t",st[i],"\t",tsb[i],"\t",tse[i],"\t",tcwq[i],"\t",tcss[i],"\t",its[i],"\t"