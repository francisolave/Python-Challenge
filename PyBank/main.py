import os
import csv

# Path to collect data from the Resources folder
budgetData_csv = os.path.join("..", "Resources", "budget_data.csv")

# Specify an output folder 
output_path = os.path.join("..", "Analysis", "budget_analysis.txt")

with open(budgetData_csv, "r") as csvFile:
    reader = csv.reader(csvFile)

    # find total number of months included in the dataset
    totalMonths = []
    for row in reader:
        total_months.append(row[0])
        total_profit.append(row[1]))
   
    total = len(totalMonths)

    # The net total amount of "Profit/Losses" over the entire period
    for i in range(len(total_profit)-1):
        
        #Changes in "Profit/Losses" over the period to find the avergae in change
        monthly_profit_change.append(total_profit[i+1]-total_profit[1])

# The greatest increase in profits (date and amount) over the entire period
    max_increase_value = max(monthly_profit_change)
    max_decrease_value = min(monthly_profit_change)

# The greatest decrease in losses (date and amount) over the entire period 
    max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
    max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

# Print statements

print("Financial Analysis")
print("------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
