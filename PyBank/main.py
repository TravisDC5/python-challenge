import os
import csv

Count = 0
monthCountArray = []
proflossTotal = []
proflossChange = []
minValue = 0
maxValue = 0
minMonth = ''
maxMonth = ''
averageChange = 0

datapath = os.path.join('resources', 'BudgetData.csv')

with open(datapath) as csvfile:

    dataparser = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(dataparser)
    

    for row in dataparser:
        
        Count += 1
        monthCountArray.append(row[0])
        proflossTotal.append(int(row[1]))
   


    for i in range(len(proflossTotal)-1): 

        proflossChange.append(proflossTotal[i+1]-proflossTotal[i])
             
        if proflossChange[i] >= maxValue:
            maxValue = proflossChange[i]
            maxMonth = monthCountArray[i+1] 
        elif proflossChange[i] <= minValue:
            minValue = proflossChange[i]
            minMonth = monthCountArray[i+1]


    averageChange = round(sum(proflossChange)/len(proflossChange),2)

    
    
    
    print(f"Total Amount of Months: {Count}")
    print(f"Total: ${sum(proflossTotal)}")
    print(f"Average Change: $ {averageChange}")
    print(f"Greatest Increase in Profits: {maxMonth}, $ {maxValue}")
    print(f"Greatest Decrease in Profits: {minMonth}, $ {minValue}")
    
    
    


