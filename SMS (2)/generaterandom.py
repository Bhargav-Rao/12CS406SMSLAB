def random(a,c,m,x0,n):
	l=[x0]
	for i in range(1,n):
		l.append((a*l[i-1]+c)%m)
	return l

def findPeriod(l):
	for i in range(len(l)):
		for j in range(i+1,len(l)):
			if(l[i]==l[j]):
				return j-i
				
print random(5,0,2**5,1,40), findPeriod(random(5,0,2**5,1,40))
print random(7,0,2**5,1,40), findPeriod(random(7,0,2**5,1,40))
print random(3,0,31,1,40), findPeriod(random(3,0,31,1,40))
# print random(3,0,31,1), findPeriod(random(3,0,31,1))