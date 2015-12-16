def calc_cum(s):
	return [sum(s[:i+1]) for i,_ in enumerate(s)]

def get_lead_time(ld):
	cum_ld = calc_cum(ld)
	rand_ld = random.random()
	return 3 if rand_ld > cum_ld[1] else (2 if rand_ld > cum_ld[0] else 1)
 
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

import random
daily_demand = [0.10,0.25,0.35,0.21,0.09]
lead_time = [0.6,0.3,0.1]
M = 11
N = 5
n = 20
starting_supply = 11

rand_demand = [random.random() for _ in range(n)]
demand = calc_cus(rand_demand,daily_demand)

table = [["SlNo","DIC","BIS","DS","EIS","SQ","OQ","LT","DLO"]]
prev =  [1,1,starting_supply,demand[0],max(starting_supply-demand[0],0),max(demand[0]-starting_supply,0),'-','-','-']

table.append(prev)
#print(demand)
for i in range(1,n):
	temp = []
	temp.append(i+1)                                           				                   # 0 SlNo - Serial No
	temp.append((i)%5+1)                                    								   # 1 DIC  - Day in Cycle
	temp.append(prev[4]+(prev[6] if prev[8]==1 else 0))      					     		   # 2 BIS  - Beginning Inventory Size
	temp.append(demand[i])                                  								   # 3 DS   - Demand Size
	temp.append(max(temp[2]-temp[3]-prev[5],0))									               # 4 EIS  - Ending Inventory Size
	temp.append(max(temp[3]-temp[2],0)+((max(prev[5]-prev[6],0) if prev[8]==1 else prev[5])))  # 5 SQ   - Order Quantity       
	if(temp[1]==N):
		temp.append(M+temp[5]-temp[4])                                                         # 6 OQ   - Order Quantity
		temp.append(get_lead_time(lead_time))                                                  # 7 LT   - Lead Time
		temp.append(temp[7])                                                                   # 8 DLO  - Days Left for Order
	else:
		temp.append(prev[6] if prev[8]!=1 else '-' )
		temp.append('-')
		temp.append((prev[8]-1) if prev[8]>1 and prev[8]!='-' else '-')
	table.append(temp)
	prev=temp

print("\n".join(("{:>8}"*9).format(*i) for i in table))