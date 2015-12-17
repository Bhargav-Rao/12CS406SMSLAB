n = 0
p = 1
lamb = 1
import math, random
ans = []
for i in range(100):
	while True:
		r = random.random()
		p*=r
		if p < (math.e ** -lamb):
			print n,r
			ans.append(n)
			break
		n+=1
