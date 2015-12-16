# Auto Correlation test for Random Numbers

def Autocorrelation(rand,i,l,const):
	print(rand)
	N = len(rand)
	m = (N - i)//l -1
	sigma = ((13*m + 7)**0.5)/float(12.0*(m+1))
	rho = (1.0/(m+1))*sum((rand[i-1+k*l]*rand[i-1+(k+1)*l]) for k in range(1,m+1)) - 0.25
	print(sum((rand[i-1+k*l]*rand[i-1+(k+1)*l]) for k in range(1,m+1)))
	print ("\n".join("{} {}".format([i-1+k*l],[i-1+(k+1)*l]) for k in range(1,m+1)))
	zo = sigma/float(rho)
	print(rho,sigma,zo)
	return "accept" if (-1*const) < zo < const else "reject"


# Generation of Random Numberss

def gen_rand(a,c,m,x):
	while True:
		x = (a*x + c)%m
		yield x

import math,random

a = [math.pow(2,34) + 1, 5, 7, 3, 5, 25173]
c = [1, 0, 0, 0, 0, 13849]
m = [math.pow(2,35), math.pow(2,5), math.pow(2,5), 31, 31, math.pow(2,1.6)]
x = [2, 1, 1, 1, 1, 1]

for i,j,k,l in zip(a,c,m,x):
	g = gen_rand(i,j,k,l)
	rand_nums = [next(g)/float(k) for _ in range(100)]
	print(i,j,k,l,Autocorrelation(rand_nums,1,5,1.6))