import csv

with open("Resources/budget_data.csv", "r") as file:
    data = csv.reader(file)
    print(data)
