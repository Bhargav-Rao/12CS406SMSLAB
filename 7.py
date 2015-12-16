# Kolmogorov Smirnov Test for Random Numbers

def KolmogorovSmirnov(rands,const):
	# D+ - max(i/N - r)
	# D- - max(r - i-1/N)
	# D  - max(D+ D-)
	N = len(rands)
	rands.sort()
	dp = max(((i/float(N)) - r) for i,r in enumerate(rands,start = 1))
	dm = max((r - (i-1)/float(N)) for i,r in enumerate(rands, start = 1))
	d = max(dp,dm)
	dn = const/math.sqrt(N)
	return ("accept" if d<dn else "reject") 

# Chi Square Test for Random Numbers

def ChiSquare(rands,const):
	bins = 10
	N = len(rands)
	slots = [1/float(bins)*i for i in range(bins)]
	freqs = [len([i for i in rands if i<j]) for j in slots]
	freqs+=[N]
	oi = [j-i for i,j in zip(freqs[:-1],freqs[1:])]
	ei = [N/float(bins) for _ in range(bins)]
	chisqr = sum(((j-i)**2)/float(i) for i,j in zip(ei,oi))
	return ("accept" if chisqr<const else "reject")


# Generation of Random Numberss

def gen_rand(a,c,m,x):
	while True:
		x = (a*x + c)%m
		yield x

import math,random

a = [math.pow(2,34) + 1, 5, 7, 3, 5, 25173]
c = [1, 0, 0, 0, 0, 13849]
m = [math.pow(2,35), math.pow(2,5), math.pow(2,5), 31, 31, math.pow(2,16)]
x = [2, 1, 1, 1, 1, 1]

for i,j,k,l in zip(a,c,m,x):
	g = gen_rand(i,j,k,l)
	rand_nums = [next(g)/float(k) for _ in range(10000000)]
	print("K",i,j,k,l,KolmogorovSmirnov(rand_nums,1.36))
	print("C",i,j,k,l,ChiSquare(rand_nums,27.2))