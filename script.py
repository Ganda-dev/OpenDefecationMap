import csv
with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        print(row['Location'] + ' - ' + row['Value'] )
