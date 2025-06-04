import actions
import csv 

students_and_grades = []


def export2csv(): #export the file to a CSV
    global students_and_grades
    with open('students.csv','w',newline='') as file:
        fields = students_and_grades[0].keys()
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(students_and_grades)


def import_csv(): #read the designated CSV file
    global students_and_grades
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
        students_and_grades = stringlist
    except FileNotFoundError:
        print('There is no csv previously exported')
