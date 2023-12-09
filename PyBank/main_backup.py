import csv
'''
Script for reading budget_data.csv file and analysing proft data. Script answers below questions
1. The total number of months included in the dataset
2. The net total amount of "Profit/Losses" over the entire period
3. The changes in "Profit/Losses" over the entire period, and then the average of those changes
4. The greatest increase in profits (date and amount) over the entire period
5. The greatest decrease in profits (date and amount) over the entire period
And redirects output to a text file in analysis folder
'''
with open('Resources/budget_data.csv', 'r') as csv_file:
    # Dict reader returns the csv data as list of dicts, where each dict is row from file
    budget_data = csv.DictReader(csv_file)
    # Casting budget data to list specifically in order to fetch length of the data
    budget_data = list(budget_data)
    # Total number of items in budget_data represents the number of months for which financial data is available, 
    # each item in the list represents data for one month
    total_number_of_months = len(budget_data)
    net_total_of_profits_over_entire_period = 0
    greatest_increase = {}
    greatest_decrease = {}
    change_sum = 0
    average_change_sum = 0
    # Iterating through budget data and adding profit/loss value for the net total value
    for row in budget_data:
        net_total_of_profits_over_entire_period = net_total_of_profits_over_entire_period  + int(row['Profit/Losses'])
    # Iterating through budget data again, to calculate profit change for each month starting from second month
    # Simultaneously, keeping track of change_sum
    # For identifying greatest increase, verifying if greatest increase value is less than current profit change, if so updating 
    # greatest increse, for calculating greatest decrease, verifying, if greatest decrease is higher than current profit change, if so
    # updating greatest decrease. Greatest increase is the highest peak, Greatest decrease is the lowest dip. 
    for i in range(1, len(budget_data)):
        # Profit for previous month
        profit_for_previous_month = int(budget_data[i-1]['Profit/Losses'])
        # Profit for current month
        profit_for_current_month = int(budget_data[i]['Profit/Losses'])                                          
        # Profit change for current month relative to last month
        profit_change = (profit_for_current_month - profit_for_previous_month)
        change_sum = change_sum + profit_change
        if not greatest_decrease or greatest_decrease['Profit_change'] > profit_change:
            greatest_decrease['Date'] = budget_data[i]['Date']
            greatest_decrease['Profit_change'] = profit_change
        if not greatest_increase or greatest_increase['Profit_change'] < profit_change:
            greatest_increase['Date'] = budget_data[i]['Date']
            greatest_increase['Profit_change'] = profit_change

    # Average sum = change_sum / number of changes
    average_change_sum = round(change_sum/(len(budget_data) - 1), 2)
    # Final output
    with open("output.txt", "w") as f:
        print("Financial Analysis\n", file=f)
        print("----------------------------\n", file=f)
        print(f"Total Months: {total_number_of_months}\n", file=f)
        print(f"Total: ${net_total_of_profits_over_entire_period}\n", file=f)
        print(f"Average Change: ${average_change_sum}\n", file=f)
        print(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Profit_change']})\n", file=f)
        print(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Profit_change']})\n", file=f)

