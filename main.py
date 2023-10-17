import csv

with open("./table_data/table_register.csv", encoding="ANSI") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
