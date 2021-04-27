# import csv

# with open('read.csv', 'r', encoding='UTF-8') as f:
#     reader  = csv.reader(f)
#     header = reader.__next__()
#     print(header)
#     print('--------------------------------------------')

# with open('read.csv', 'r', encoding='UTF-8') as f:
#     reader  = csv.reader(f)
#     body = next(reader)

#     for row in reader:
#         print(row)



import pandas as pd

df_header = pd.read_csv('read.csv')
print(df_header.to_string(index=False))
