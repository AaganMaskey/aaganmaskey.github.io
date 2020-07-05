import csv
def write_in_csv(filename, list0):
    head_content = ('Name', 'Address', 'Age')
    csvfile = open(filename, 'w', newline='')
    obj = csv.writer(csvfile)
    obj.writerow(head_content)
    obj.writerows(list0)
    csvfile.close()
lst = [('Anthony', 'London', 25), ('Akbar', 'USA', 23), ('Amar', 'Australia', 22)]
write_in_csv("user_list.csv", lst)
print("Data stored in CSV file")