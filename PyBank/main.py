import os
import csv

datapath = os.path.join('g','DataBootCamp','PythonWork','python-challenge','PyBank','resources', 'BudgetData.csv')

with open(datapath) as csvfile:

    dataparser = csv.reader(csvfile, delimiter=',')

    csv_header = next(dataparser)

    for row in dataparser:
        print(row[0])
        