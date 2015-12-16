# Monte Carlo Simulation

vel = 10
thresh = 50
end_time = 100
maxval = 100
from random import randint

xb = randint(1,maxval)
yb = randint(1,maxval)

xf = randint(1,maxval)
yf = randint(1,maxval)

xfs = [xf]
yfs = [yf]
xbs = [xb]
ybs = [yb]

for i in range(1,end_time):
	d = ((yfs[i-1]-ybs[i-1])**2 + (xfs[i-1]-xbs[i-1])**2)**0.5
	print(d)
	if d<= thresh:
		print("Success")
		break
	xb = randint(1,maxval)
	yb = randint(1,maxval)

	xbs.append(xb)
	ybs.append(yb)

	sin = (ybs[i-1]-yfs[i-1])/float(d)
	cos = (xbs[i-1]-xfs[i-1])/float(d)

	xfs.append(xfs[i-1]+vel*cos)
	yfs.append(yfs[i-1]+vel*sin)
else:
	print("Escaped")