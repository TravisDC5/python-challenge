import os
import csv

monthsCount = 0
monthCountArray = []
proflossTotal = []
proflossChange = []

datapath = os.path.join('resources', 'BudgetData.csv')

with open(datapath) as csvfile:

    dataparser = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(dataparser)
    'minValue, maxValue = [], []'
    dataArray = []

    for row in dataparser:
        
        monthsCount += 1
        monthCountArray.append(row[0])
        proflossTotal.append(int(row[1]))
        'proflossTotal = proflossTotal + int(row[1])'
       


    
    
    print(f"Total Amount of Months: {monthsCount}")
    print(f"Total: ${sum(proflossTotal)}")
    
   