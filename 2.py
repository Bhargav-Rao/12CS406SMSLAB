def calc_stats(a,b,c):
	temp = []
	for i,v in enumerate(a):
		for k,j in enumerate(b):
			if v<j:
				temp.append(k+1)
				break
		else:
			temp.append(len(c))
	return temp

sts = [0.05, 0.05, 0.1, 0.2, 0.3, 0.3]
cum_sts = [sum(sts[:i+1]) for i,_ in enumerate(sts)]

iats = [0.125] * 8
cum_iats = [0.125*i for i in range(1,8)]

n = 20

import random

cus_sts_rands = [random.random() for _ in range(n)]
cus_iats_rands = [random.random() for _ in range(n)]

cus_iats = calc_stats(cus_iats_rands,cum_iats,iats)
cus_sts = calc_stats(cus_sts_rands,cum_sts,sts)

table = [["Slno","IAT","AT","ST","TSB","TSE" ,"TTSS","TWT","TITS"]]

prev = [0 ,'-' ,0, cus_sts[0] ,0,cus_sts[0], cus_sts[0],0,0 ]
table.append(prev)

for i in range(1,n-1):
	temp = [i+1]                                      # 0 SLNO  - Serial Number
	temp.append(cus_iats[i-1])                        # 1 IAT   - Inter Arrival Time
	temp.append(cus_iats[i-1]+prev[2])                # 2 AT    - Arrival Time
	temp.append(cus_sts[i])                           # 3 ST    - Service Time
	temp.append(max(temp[2],prev[5]))                 # 4 TSB   - Time Service Begins
	temp.append(temp[4]+temp[3])                      # 5 TSE   - Time Service Ends
	temp.append(temp[5]-temp[2])                      # 6 TTSS  - Total Time Spent in Server
	temp.append(temp[4]-temp[2])                      # 7 TWT   - Total Waiting Time 
	temp.append(prev[8]+max((temp[4]-prev[5]),0))     # 8 TITS  - Total Idle Time of Server
	table.append(temp)
	prev = temp

print('\n'.join(("{:<7}"*9).format(*i) for i in table))