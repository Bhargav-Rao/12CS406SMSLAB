def calc_cum(s):
	return [sum(s[:i+1]) for i,_ in enumerate(s)]

def calc_papers(day_type,types):
	values = types[day_type]
	cum_values = calc_cum(values)
	demands = list(range(40,101,10))
	rand_int = random.random()
	for i,v in enumerate(cum_values):
		if rand_int < v:
			return demands[i]

buy = 33 
sel = 50 
scrap = 5 
bundle = 10
N = 5
n = 20
types = {
			"good" : [0.03,0.05,0.15,0.20,0.35,0.15,0.07] ,
			"fair" : [0.10,0.18,0.40,0.20,0.08,0.04,0.00] ,
			"poor" : [0.44,0.22,0.16,0.12,0.06,0.00,0.00] 
		}
probs = [0.35, 0.45, 0.20]
import random

rand_days = [random.random() for _ in range(n)]
cum_probs = calc_cum(probs)
days = ["good" if i>cum_probs[1] else ("fair" if i>cum_probs[0] else "poor") for i in rand_days]
papers_demand = [calc_papers(day_type,types) for day_type in days]
papers_bought = N*bundle

table = [["Slno","DT","DPD","PB","DIF","DC","PFS","LED","PSFS","TPD"]]

for i in range(n):
	temp = []
	temp.append(i+1)                                   # 0 SlNO  - Serial No/ Day No
	temp.append(days[i])                               # 1 DT    - Demand Type
	temp.append(papers_demand[i])                      # 2 DPD   - Demand per day
	temp.append(papers_bought)                         # 3 PB    - Papers Bought
	temp.append(temp[2]-temp[3])                       # 4 DIF   - Difference in Demand and Bought / Excess Demand
	temp.append(temp[3]*buy)                           # 5 DC    - Daily Cost of Paper
	temp.append(min(temp[2],temp[3])*sel)              # 6 PFS   - Profit from Sales
	temp.append(max((temp[2]-temp[3])*sel,0))          # 7 LED   - Loss from Excess Demand
	temp.append(max((temp[3]-temp[2])*scrap,0))        # 8 PSFS  - Profit Salvaged From Scrap
	temp.append(temp[6]-temp[5]-temp[7]+temp[8])       # 9 TTD   - Total Profit Per Day
	table.append(temp)

print("\n".join(("{:>8}"*10).format(*i) for i in table))