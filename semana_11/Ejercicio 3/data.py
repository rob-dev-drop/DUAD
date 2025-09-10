import actions
import csv 

class Student():
    def __init__(self, name, room, sp_grade, en_grade, ss_grade, sc_grade, avg):
        self.name = name
        self.room = room
        self.sp_grade = sp_grade
        self.en_grade = en_grade
        self.ss_grade = ss_grade
        self.sc_grade = sc_grade
        self.avg = avg

def export2csv(saved): #export the file to a CSV
    with open('students.csv','w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["name","room","spanish","english","social","science","average"])
        for i in saved:
            writer.writerow([i.name, i.room, i.sp_grade, i.en_grade, i.ss_grade, i.sc_grade, i.avg])


def import_csv(): #read the designated CSV file
    list = []
    try:
        with open('students.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                new_student = Student(
                    row[0], #name
                    row[1], #room
                    int(row[2]), #spanish
                    int(row[3]), #english
                    int(row[4]), #social
                    int(row[5]), #science
                    float(row[6]), #average
                    )
                list.append(new_student)
        return list
    except FileNotFoundError:
        print('There is no csv previously exported')
