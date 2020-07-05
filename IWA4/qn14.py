import csv
list = []
def read_csv(filename):
    csvfile = open(filename, 'r', newline='')
    obj = csv.DictReader(csvfile)
    for row in obj:
        list.append(dict(row))
    print(list)
read_csv("user_list.csv")