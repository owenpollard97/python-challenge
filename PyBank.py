import os
import csv
import pandas as pd

# Get the current working directory
current_dir = os.getcwd()

#Correct File Path
file_path = 'C:/New folder/budget_data.csv'

#Output File
output_file = 'C:/New folder/analysis.text'

# Opening csv File
with open(file_path, 'r') as budget_data:
    
# Creating My CSV Reader
    csvreader = csv.reader(budget_data)

    # Variable Declarations
    greatest_increase_in_profits = ['', 0]
    greatest_decrease_in_profits = ['', 9999999999]
    total_months = 0
    total_loss_in_profit = 0
    previous_profit_loss = 0
    change_in_profit = 0

    # Skip Headers
    next(csvreader)

    # Looping Through CSV Rows
    for row in csvreader:
        # Total Months
        total_months += 1

        # P&L Overall
        print(row)
        total_loss_in_profit += int(row[1])

        # Difference in P&L Between Rows
        change_in_profit = int(row[1]) - previous_profit_loss
        previous_profit_loss = int(row[1])

        # Greatest Profit Increase
        if change_in_profit > greatest_increase_in_profits[1]:
            greatest_increase_in_profits[0] = row[0]
            greatest_increase_in_profits[1] = change_in_profit

        # Greatest Profit Decrease
        if change_in_profit < greatest_decrease_in_profits[1]:
            greatest_decrease_in_profits[0] = row[0]
            greatest_decrease_in_profits[1] = change_in_profit

    # Average P&L Changes
    average_change = round(total_loss_in_profit / total_months, 2)

    # Analysis Results
    print("Financial Analysis")
    print(average_change)
    print("---------")
    print(f"Total Months: {total_months}")
    print(f"Greatest Profit Increase: {greatest_increase_in_profits[0]} (${greatest_increase_in_profits[1]})")
    print(f"Greatest Profit Decrease: {greatest_decrease_in_profits[0]} (${greatest_decrease_in_profits[1]})")

    #Exporting Results
with open(output_file, 'w') as analysis_file:
    analysis_file.write("Financial Analysis\n")
    analysis_file.write("---------\n")
    analysis_file.write(f"Total Months: {total_months}\n")
    analysis_file.write(f"Greatest Profit Increase: {greatest_increase_in_profits[0]} (${greatest_increase_in_profits[1]})\n")
    analysis_file.write(f"Greatest Profit Decrease: {greatest_decrease_in_profits[0]} (${greatest_decrease_in_profits[1]})\n")

print("Results exported to analysis.txt file.")