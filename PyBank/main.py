#Import the module to use to make new path directories
import os
#Import in csv
import csv

#join the path 
financial_data = os.path.join("..","Resources", "budget_data.csv")

# Open and read the csv to report findings into variables
with open(financial_data, newline="") as csvfile: 
    #Store the data into variable
    csvreader = csv.reader(csvfile, delimiter=",")
    #Make sure to skip the header as input
    csvheader = next(csvreader)

#Generate lists to loop through the rows for each variable

total_months = []
total_profit = []
monthly_profit_change = []

    #Loop through the data for total months and total profit
    for row in csvreader:

        #Attach the total months and total profit to their specific lists
        total_months.append([row(0)])
        #Make sure to make profit recognizable as an integer and not a string
        total_profit.append(int(row[1]))
    
    #Loop through the months to generate the change in profit
    for i in range(len(total_profit)-1):
        #The difference between every two months is the monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])

#Greatest Increase in Profits
max_increase_value = max(monthly_profit_change)
#Greatest Decrease in Profits
max_decrease_value = min(monthly_profit_change)

#Associate max and min values to each month through indexing by adding 1 and looping through the month list
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

#Print out all the Statements in the correct order to appear in text file
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

#Output files to a text file
file = open("output.txt","w")

#Write out how answers will be displayed in text file 
    file.write("Financial Analysis" +"\n")
    file.write("\n")
    file.write("----------------------------" + "\n")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}" + "\n")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}" + "\n")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}" + "\n")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} + (${(str(max_increase_value))})" + "\n")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} + (${(str(max_decrease_value))})" + "\n")
    file.close()