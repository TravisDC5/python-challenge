# Import Module
import os
import csv


#Declare and Initialize variables


# Read-In csv file containing raw data
datapath = os.path.join('resources', 'BudgetData.csv')

with open(datapath) as csvfile:

    dataparser = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(dataparser)
    pValue = next(dataparser)
    
    Count = 1
    netProfit = int(pValue[1])
    averageChange = []
    minValue = 0
    maxValue = 0
    minMonth = ''
    maxMonth = ''
    
    
    #Extract useful data to be used later for running calculations/mainuplations
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
       
    netChange = sum(averageChange)/len(averageChange)
    
    #Print to terminal final values
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Amount of Months: {Count}")
    print(f"Total: ${(netProfit):.2f}")
    print(f"Average Change: $ {(netChange):.2f}")
    print(f"Greatest Increase in Profits: {maxMonth}, $ {maxValue}")
    print(f"Greatest Decrease in Profits: {minMonth}, $ {minValue}")

      

    Output file with final values
output_file = os.path.join("analysis", "FinancialAnalysis.txt")

with open(output_file,"w") as file:     
    
    file.write("Financial Analysis \n")
    file.write("----------------------------\n")
    file.write(f"Total Amount of Months: {Count}\n")
    file.write(f"Total: ${sum(proflossTotal)}\n")
    file.write(f"Average Change: $ {averageChange}\n")
    file.write(f"Greatest Increase in Profits: {maxMonth}, $ {maxValue}\n")
    file.write(f"Greatest Decrease in Profits: {minMonth}, $ {minValue}")