def get_random(a,c,m,x):
	while True:
		x = (a * x + c) % (m)
		yield x

import math

a = [math.pow(2,34) + 1, 5, 7, 3, 5, 25173]
c = [1, 0, 0, 0, 0, 13849]
m = [math.pow(2,35), math.pow(2,5), math.pow(2,5), 31, 31, math.pow(2,16)]
x = [2, 1, 1, 1, 1, 1]


for i,j,k,l in zip(a,c,m,x):
	g = get_random(i,j,k,l)
	rand_nums = [next(g) for i in range(100)]
	print(len(set(rand_nums)))