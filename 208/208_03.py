import csv


with open('read.csv', 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    
    for row in reader:
        print(row)