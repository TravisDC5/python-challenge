import os
import csv
monthsCount = 0
proflossTotal = 0

datapath = os.path.join('resources', 'BudgetData.csv')

with open(datapath) as csvfile:

    dataparser = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(dataparser)

    

    for row in dataparser:
        
        monthsCount += 1
        proflossTotal = proflossTotal + int(row[1])
    
    
    
    print(f"Total Amount of Months: {monthsCount}")
    print(f"Total Profit/Loss = ${proflossTotal}")    