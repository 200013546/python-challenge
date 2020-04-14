# First Import Modules
import os
import csv

# Create Variables
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Get File Path
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# Open & Read CSV File
with open(csvpath, newline='') as csvfile:
    
    # CSV Reader Specifies Delimiter & Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read The Header Row First (Skip This Step If There Is No Header)
    csv_header = next(csvreader)
    row = next(csvreader)
    
    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The average of the changes in "Profit/Losses" over the entire period
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in losses (date and amount) over the entire period
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    # Get Each Row of Data After the Header
    for row in csvreader:
        
        # Get Total Number of Months Included in Dataset
        total_months += 1
        # Get Net Amount of "Profit/Losses" Over the Period
        net_amount += int(row[1])

        # Get Change from Current Month to Previous Month
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        # Get the Greatest Increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # Get the Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
    # Get the Average and the Date
    average_change = sum(monthly_change)/ len(monthly_change)
    
    highest = max(monthly_change)
    lowest = min(monthly_change)

# Print Analysis
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${highest})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${lowest})")

# Specify File to Write to
output_file = os.path.join('.', 'Resources', 'budget_data_revised.text')

# Open File Using "Write" Mode and Specify the Variable to Hold the Contents
with open(output_file, 'w',) as textfile:

# Write New Data
    textfile.write(f"Financial Analysis\n")
    textfile.write(f"---------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${net_amount}\n")
    textfile.write(f"Average Change: ${average_change:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${highest})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${lowest})\n")
