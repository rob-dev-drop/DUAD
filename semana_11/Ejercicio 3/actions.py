import data

class Student():
    def __init__(self, name, room, sp_grade, en_grade, ss_grade, sc_grade, avg):
        self.name = name
        self.room = room
        self.sp_grade = sp_grade
        self.en_grade = en_grade
        self.ss_grade = ss_grade
        self.sc_grade = sc_grade
        self.avg = avg

def input_student(): # asks for the information that is required in the program
    data_name = input("Enter student Name: ")
    data_room = input("Enter room number: ")
    print('Enter Spanish Grade: ')
    data_grade_sp = validate_grade()
    print('Enter English Grade: ')
    data_grade_en = validate_grade()
    print('Enter Social Studies Grade: ')
    data_grade_ss = validate_grade()
    print('Enter Science Grade: ')
    data_grade_sc = validate_grade()
    average = calculate_avg(data_grade_ss,data_grade_en,data_grade_sc,data_grade_sp)

    def create_student():
        x = Student(data_name,data_room,data_grade_sp,data_grade_en,data_grade_ss,data_grade_sc,average)
        return x
    
    student = create_student() # Creo que necesito cambiar todo el input aunque no estoy del todo seguro. Me imagino que tengo que hacer una lista de objetos y creo que el objeto de estudiante tiene que ponerse en una lista. por ahora ya tengo la clase de estudiante hecha
    
    return student


def validate_grade(): 
    valid = False
    while valid == False:
        try:
            x = int(input())
            if x >= 0 and x <= 100:
                valid = True
                return x
            else:
                raise ValueError()
        except ValueError:
            print('Grade must be between 0 and 100')


def add_student(): #trigger for option 1
    xy = input_student()
    print('Student added')
    return xy


def show_students(param): #Shows students, their room and grades
    print('These are the students in the database:')
    for num in param:
        print(f'{num.name} from room {num.room}')
        print('-------Grades-------')
        print(f'    Spanish: {num.sp_grade}')
        print(f'    English: {num.en_grade}')
        print(f'Social Studies: {num.ss_grade}')
        print(f'    Science: {num.sc_grade}')
        print(f'    Average: {num.avg}')
        print('---------------------')


def calculate_avg(grade1, grade2, grade3, grade4): #calculates the average to add it right away into the dictionary that each student is
    grades2sum = [grade1, grade2, grade3, grade4]
    average = sum(grades2sum) / 4
    return average


def compare_avg(param):    #Compares the average of all students already input
    top1name = ""
    top1 = 0
    top2name = ""
    top2 = 0
    top3name = ""
    top3 = 0
    for student in param:
        done = False
        avg_grade = student.avg
        while done == False:
            if avg_grade > top1:
                top3 = top2
                top3name = top2name
                top2 = top1 
                top2name = top1name
                top1 = avg_grade
                top1name = student.name
                done = True
            elif avg_grade > top2:
                top3 = top2
                top3name = top2name
                top2 = avg_grade
                top2name = student.name
                done = True
            elif avg_grade > top3:
                top3 = avg_grade
                top3name = student.name
                done = True
            else:
                done = True

    print(f'Top 3 Students:')
    print(f'{top1name} with an average of {top1}')
    print(f'{top2name} with an average of {top2}')
    print(f'{top3name} with an average of {top3}')


def show_average_of_avegares(param): #shows average of all averages from all students
    list_of_averages = []
    for student in param:
        list_of_averages.append(student.avg)
    final_average = sum(list_of_averages)/len(list_of_averages)
    print(f'The average of all registered students is {final_average}')

