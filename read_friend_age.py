import csv

with open("./csvData/my_friends.csv", "r") as file:
    lines = csv.reader(file)
    header = next(lines)
    for line in lines:
        print(line)
