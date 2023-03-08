# import the modules required for the program

import csv
import os
# Define the source  path for the  csv file
file_path = r"Pybank/Resources/budget_data.csv"
#Define the source path for the result text file in the analysis folder
result_path = r"Pybank/Analysis/PyBank_resultstest.txt"
# Get the list for the months, net profit and net change and initilize the total to zero
months = []
total = 0
net_profit = []
net_change =[]

# open the file
with open(file_path) as file:
    filereader = csv.reader(file, delimiter=",") # demlmiter for the comma seperated values
    header = next(filereader) #skip the header
    for row in filereader: #start the loop from the second row
        months.append(row[0]) # for each row add the month to the months list
        total = total + int(row[1]) #keep on adding the rows
        net_profit.append(int(row[1])) # make a list for the profit/loss column
   
#from the  profit list and subtract values one by one to see the net change,append the empty list by these values and then get the average.
Difference = 0             
for each in range(len(net_profit)):
    if each < len(net_profit) - 1: # we have to subtract -1 because otherwise
        Difference = Difference + (net_profit[each + 1] - net_profit[each])
        net_change.append(Difference)
        Difference = 0


#now get the average change ,the min and max values from the profit/loss list
average_change = round(sum(net_change) / len(net_change),3)

decrease_Profit = min(net_change)

increase_Profit = max(net_change)

# To gst the months for the corresponding chnages 1 s added for the index because length of months is 86 and that of net chnage is 85 due to one by one subtraction
decrease_month = months[net_change.index(decrease_Profit)+1]
increase_month = months[net_change.index(increase_Profit)+1]

# write the reuls in the text file
with open(result_path, 'x', newline='') as wf: 
    
    wf.write(f"Financial Analysis\n")
    wf.write(f"_ _ _ _ _ _ _ _ _ _\n")
    wf.write(f"Total Months {len(months)} \n")
    wf.write(f"Total : $ {total}\n")
    wf.write(f"Average Change: $ {average_change}\n")
    wf.write(f"Greatest Increase in Profits: {increase_month} ( $ {increase_Profit})\n")
    wf.write(f"Greatest Dncrease in Profits: {decrease_month} ( $ {decrease_Profit})\n")
# print the result to the terminal
with open(result_path) as f:
    lines = f.readlines()
    for each in lines:
        print(each)