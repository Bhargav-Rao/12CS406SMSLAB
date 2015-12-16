def calc_cum(s):
	return [sum(s[:i+1]) for i,_ in enumerate(s)]

def calc_cus(rand_vals,set_vals):
	temp = []
	for _, v in enumerate(rand_vals):
		for num, iat in enumerate(calc_cum(set_vals)):
			if v< iat:
				temp.append(num+1)
				break
		else:
			temp.append(len(set_vals))
	return temp

iats = [0.25,0.40,0.20,0.15]
sts_abl = [0.3,0.28,0.25,0.17]
sts_bak = [0.35,0.25,0.2,0.2]

n = 25

import random

rand_iats = [random.random() for _ in range(n-1)]
rand_sts  = [random.random() for _ in range(n)]

cus_iats    = calc_cus(rand_iats,iats)
cus_sts_abl = calc_cus(rand_sts,sts_abl)
cus_sts_bak = calc_cus(rand_sts,sts_bak)

table = [["SlNo","IAT","AT","ST","SBA","SEA","ITA","SBB","SEB","ITB","TCSQ"]]

prev = [1,'-',0,cus_sts_abl[0],0,cus_sts_abl[0],0,'-','-','-',0]

table.append(prev)

for i in range(1,n):
	temp = [i+1]                                                           # SlNo
	prev = [0 if i=='-' else i for i in prev ]
	temp.append(cus_iats[i-1])                                             # IAT
	temp.append(prev[2]+temp[1])                                           # AT
	if(prev[5]=='-' or temp[2]>prev[5]):
		server = 'a'
	elif(prev[8]=='-' or temp[2]>prev[8]):
		server = 'b'
	else:				
		server = 'a' if (prev[5]<prev[8]) else 'b'
	temp.append(cus_sts_abl[i] if server=='a' else cus_sts_bak[i])         # ST
	if server=='a':
		temp.append(max(prev[5],temp[2]))                                  # SBA
		temp.append(temp[4]+temp[3])                                       # SEA
		temp.append(max((prev[5]-temp[2]),0))                              # ITA
		temp.extend(['-','-','-'])                                         # SERVER B Stuff
	elif server=='b':
		temp.extend(['-','-','-'])                                         # SERVER A Stuff
		temp.append(max(prev[8],temp[2]))                                  # SBB
		temp.append(temp[7]+temp[3])                                       # SEB
		temp.append(max((prev[8]-temp[2]),0))                              # ITB
	temp.append((temp[4] if server=='a' else temp[7]) -temp[2])            # TCSQ
	table.append(temp)
	prev = temp

print("\n".join(("{:<7}"*11).format(*i) for i in table))