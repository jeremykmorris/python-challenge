# Your task is to create a Python script that analyzes the records to calculate each of the following values:

# Your analysis should align with the following results:

    # Financial Analysis
    # ----------------------------
    # Total Months: 86
    # Total: $22564198
    # Average Change: $-8311.11
    # Greatest Increase in Profits: Aug-16 ($1862002)
    # Greatest Decrease in Profits: Feb-14 ($-1825558)

import os
import csv

csvpath = os.path.join(r'C:\Users\Jeremy Morris\OneDrive\Desktop\OSU Data Analysis Course\Modules\Module 3 Python Challenge\PyBank\Resources\budget_data.csv')

#variables
totalmonths = []
profits = []
pl = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        totalmonths.append(row[0])
        profits.append(int(row[1]))
for i in range(len(profits) - 1):
    pl.append(profits[i+1] - profits[i])

total_months = len(totalmonths)
sum_profits = sum(profits)
avg_change = (sum(pl) / len(pl))
greatest_increase = ((totalmonths[pl.index(max(pl))+1]))
greatest_decrease = ((totalmonths[pl.index(min(pl))+1]))
m_increase = max(pl)
m_decrease = min(pl)

print('Financial Analysis')
print('----------------------------')
print(f'Total Months; {total_months}')
print(f'Total: ${sum_profits}')
print(f'Average Change: ${avg_change}')
print(f'Greatest Increase in Profits: {greatest_increase} (${m_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease} (${m_decrease})')

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

#Print results to text file
output_folder = r'C:\Users\Jeremy Morris\OneDrive\Desktop\OSU Data Analysis Course\Modules\Module 3 Python Challenge\PyBank\analysis'
output_file = os.path.join(output_folder, 'PyBank_results.txt')

with open(output_file, "w") as file:
    file.write('Financial Analysis\n')
    file.write('----------------------------\n')
    file.write(f'Total Months; {total_months}\n')
    file.write(f'Total: ${sum_profits}\n')
    file.write(f'Average Change: ${avg_change}\n')
    file.write(f'Greatest Increase in Profits: {greatest_increase} (${m_increase})\n')
    file.write(f'Greatest Decrease in Profits: {greatest_decrease} (${m_decrease})\n')
    