# Import Module
import os
import csv

# Read-In csv file containing raw data 
datapath = os.path.join('resources', '03-Python_HW_Instructions_PyBank_Resources_budget_data.csv')

with open(datapath) as csvfile:

    dataparser = csv.reader(csvfile, delimiter=',')
    
    # 1st next() skips over header of read-in file, 2nd next() stores first row of data for processing later
    csv_header = next(dataparser)
    pValue = next(dataparser)
    
    #Declare and Initialize essential variables
    Count = 1
    netProfit = int(pValue[1])
    averageChange = []
    minValue = 0
    maxValue = 0
    minMonth = ''
    maxMonth = ''
    
    
    #iterates through raw data, and pulls values for calculating the objective outputs
    for row in dataparser:
        
        Count += 1
        netProfit = netProfit + int(row[1])
        differenceProfit = int(row[1])-int(pValue[1])
        averageChange.append(differenceProfit)

        if differenceProfit >= maxValue:
            maxValue = differenceProfit
            maxMonth = row[0] 
        elif differenceProfit <= minValue:
            minValue = differenceProfit
            minMonth = row[0]


        
        pValue[1] = int(row[1])

    # Calculate the sum of all average differences   
    netChange = sum(averageChange)/len(averageChange)
    
    #Print to terminal final values
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Amount of Months: {Count}")
    print(f"Total: ${(netProfit):.2f}")
    print(f"Average Change: $ {(netChange):.2f}")
    print(f"Greatest Increase in Profits: {maxMonth}, $ {maxValue}")
    print(f"Greatest Decrease in Profits: {minMonth}, $ {minValue}")

      

# Output file with final values
output_file = os.path.join("analysis", "FinancialAnalysis.txt")

with open(output_file,"w") as file:     
    
    file.write("Financial Analysis \n")
    file.write("----------------------------\n")
    file.write(f"Total Amount of Months: {Count}\n")
    file.write(f"Total: ${(netProfit):.2f}\n")
    file.write(f"Average Change: $ {(netChange):.2f}\n")
    file.write(f"Greatest Increase in Profits: {maxMonth}, $ {maxValue}\n")
    file.write(f"Greatest Decrease in Profits: {minMonth}, $ {minValue}")