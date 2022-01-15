# import dependencies
import os
import csv

# grabbing the csv needed for the assignment
budget_csv = os.path.join("Resources", "budget_data.csv")

# Create variables and lists
date = []
profit = []
monthly_change = []

count = 0
net_profits = 0
last_month_profit = 0
current_month_profit = 0
change_in_profit  = 0


# read csv file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

# iterate through each row in csv file to find total months and total profit, then add each date and monthly change to the lists    
    for row in csvreader:
        count = count + 1
        net_profits = int(row[1]) + net_profits
        date.append(row[0])
        current_month_profit = int(row[1])
        if count >= 1: 
           change_in_profit = current_month_profit - last_month_profit
           monthly_change.append(change_in_profit)
           last_month_profit = int(row[1]) 

# deleted unessary value in list. Calculated average change and the greatest and lowest monthly change with the dates attached
monthly_change.pop(0)
avg_change = round(sum(monthly_change)/len(monthly_change),2)
greatest_increase = max(monthly_change)
greatest_decrease = min(monthly_change)

increase_date = date[monthly_change.index(greatest_increase) + 1]
decrease_date = date[monthly_change.index(greatest_decrease) + 1]

#print results
print("Financial Analysis \n----------------------------")
print(f"Total Months: {count}")
print(f"Total: ${net_profits}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")

# exporting text file with my results
f = open('finanacial_analysis.txt', 'w')

with open('finanacial_analysis.txt', 'w') as f:
    f.write("Financial Analysis \n----------------------------")
    f.write(f"\nTotal Months: {count}")
    f.write(f"\nTotal: ${net_profits}")
    f.write(f"\nAverage Change: ${avg_change}")
    f.write(f"\nGreatest Increase in Profits: {increase_date} (${greatest_increase})")
    f.write(f"\nGreatest Decrease in Profits: {decrease_date} (${greatest_decrease})")





        
        

