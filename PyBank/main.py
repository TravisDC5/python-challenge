import os
import csv
monthsCount = 0
datapath = os.path.join('resources', 'BudgetData.csv')

with open(datapath) as csvfile:

    dataparser = csv.reader(csvfile, delimiter=',')

    csv_header = next(dataparser)

    """for row in dataparser:
        'monthsCount = len(row[0])
    """  
    monthsCount = len(list(dataparser))

    print(f"Total Amount of Months: {monthsCount}")
        