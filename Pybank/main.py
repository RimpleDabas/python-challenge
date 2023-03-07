import csv
import os
file_path = r"Pybank/Resources/budget_data.csv"
result_path = r"Pybank/Analysis/PyBank_results.txt"
months = []
total = 0
net_profit = []
net_change =[]



with open(file_path) as file:
    filereader = csv.reader(file, delimiter=",")
    header = next(filereader)
    
    for row in filereader:
        #print(row)
        #break
        months.append(row[0])
        total = total + int(row[1])
        net_profit.append(int(row[1]))
#print(net_profit)    

Difference = 0             
for each in range(len(net_profit)):
    if each < len(net_profit) - 1:
        Difference = Difference + (net_profit[each + 1] - net_profit[each])
        net_change.append(Difference)
        Difference = 0

#print(len(net_change))
average_change = round(sum(net_change) / len(net_change),3)
#print(average_change)
decrease_Profit = min(net_change)
#print(decrease_Profit)
increase_Profit = max(net_change)
#print(increase_Profit)

decrease_month = months[net_change.index(decrease_Profit)+1]
increase_month = months[net_change.index(increase_Profit)+1]
#print(increase_month)
#print(decrease_month)
#print(total)
#print(len(months))  

with open(result_path, 'x', newline='') as wf: 
    
    wf.write(f"Financial Analysis\n")
    wf.write(f"_ _ _ _ _ _ _ _ _ _\n")
    wf.write(f"Total Months {len(months)} \n")
    wf.write(f"Total : $ {total}\n")
    wf.write(f"Average Change: $ {average_change}\n")
    wf.write(f"Greatest Increase in Profits: {increase_month} ( $ {increase_Profit})\n")
    wf.write(f"Greatest Dncrease in Profits: {decrease_month} ( $ {decrease_Profit})\n")

with open(result_path) as f:
    lines = f.readlines()
    for each in lines:
        print(each)