import os
import csv

# Can't figure out my path but I'm gonna try and write the code (won't know if it works)

# Set Path
csvpath = os.path.join('"..", "Resources", "budget_data.csv"')

# Open & Read CSV File
with open(csvpath,) as csvfile:


#variables
NumMonths = 0
Net_total = 0
total_Profit_Losses = 0
profit_change = []
greatest_increase = 0
greatest_decrease = 0


for row in csvreader: 

#calculate Month Totals
 Num_months += 1
 previous_row = int(row[1])

#calculate Net Total
Net_total += int(row[1])
previous_row = int(row[1])







