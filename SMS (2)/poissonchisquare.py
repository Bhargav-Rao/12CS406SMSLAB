import math
val=[0,1,2,3,4,5,6]
o=[35,40,13,6,4,1,1]
alpha = sum([val[i]*o[i] for i in range(len(val))])/float(sum(o))

p = [(math.e**-alpha)*(alpha**i)/float(math.factorial(i)) for i in range(len(val))]
# print p
e = [p[i]*100 for i in range(len(p))]
print e

i = 0
while i < (len(e)):
	while i+1 < (len(e)) and e[i]<5:
		e[i] = sum(e[i:i+2])
		o[i] = sum(o[i:i+2])
		e.pop(i+1)
		o.pop(i+1)
	i+=1

if(e[-1]<5):
	e[-1-1] = e[-1-1]+e[-1]
	o[-1-1] = o[-1-1]+o[-1]
	e.pop(-1)
	o.pop(-1)
	
x0sq = sum([(((o[i]-e[i])**2)/float(e[i])) for i in range(len(o))])
print "classess=",len(o)

print "accepted" if x0sq<9.49 else "rejected"