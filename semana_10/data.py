import actions
import csv 


def export2csv(saved): #export the file to a CSV
    with open('students.csv','w',newline='') as file:
        fields = saved[0].keys()
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(saved)


def import_csv(): #read the designated CSV file
    try:
        with open('students.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            stringlist = list(reader)
        for row in stringlist: #Turn the numbers into int since they are stored as str (float for average)
            row['Spanish'] = int(row['Spanish'])
            row['Social Studies'] = int(row['Social Studies'])
            row['Science'] = int(row['Science'])
            row['English'] = int(row['English'])
            row['average'] = float(row['average'])
        return stringlist
    except FileNotFoundError:
        print('There is no csv previously exported')
