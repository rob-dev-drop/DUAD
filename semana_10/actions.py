import data


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
    student = {
        'name':'name_d',
        'room':'room_d',
        'Spanish': 999,
        'English': 999,
        'Social Studies': 999,
        'Science': 999,
        'average': 0
        }
    student['name'] = data_name
    student['room'] = data_room
    student['Spanish'] = data_grade_sp
    student['English'] = data_grade_en
    student['Social Studies'] = data_grade_ss
    student['Science'] = data_grade_sc
    student['average'] = calculate_avg(data_grade_sp, data_grade_en, data_grade_ss, data_grade_sc)
    
    return student


def validate_grade(): # need to correct the logic
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
    data.students_and_grades.append(input_student())
    print('Student added')


def show_students(): #Shows students, their room and grades
    print('These are the students in the database:')
    for num in data.students_and_grades:
        print(f'{num['name']} from room {num['room']}')
        print('-------Grades-------')
        print(f'    Spanish: {num['Spanish']}')
        print(f'    English: {num['English']}')
        print(f'Social Studies: {num['Social Studies']}')
        print(f'    Science: {num['Science']}')
        print(f'    Average: {num['average']}')
        print('---------------------')


def calculate_avg(grade1, grade2, grade3, grade4): #calculates the average to add it right away into the dictionary that each student is
    grades2sum = [grade1, grade2, grade3, grade4]
    average = sum(grades2sum) / 4
    return average


def compare_avg():    #Compares the average of all students already input
    top1name = ""
    top1 = 0
    top2name = ""
    top2 = 0
    top3name = ""
    top3 = 0
    for student in data.students_and_grades:
        done = False
        avg_grade = student['average']
        while done == False:
            if avg_grade > top1:
                top3 = top2
                top3name = top2name
                top2 = top1 
                top2name = top1name
                top1 = avg_grade
                top1name = student['name']
                done = True
            elif avg_grade > top2:
                top3 = top2
                top3name = top2name
                top2 = avg_grade
                top2name = student['name']
                done = True
            elif avg_grade > top3:
                top3 = avg_grade
                top3name = student['name']
                done = True
            else:
                done = True

    print(f'Top 3 Students:')
    print(f'{top1name} with an average of {top1}')
    print(f'{top2name} with an average of {top2}')
    print(f'{top3name} with an average of {top3}')


def show_average_of_avegares(): #shows average of all averages from all students
    list_of_averages = []
    for student in data.students_and_grades:
        list_of_averages.append(student['average'])
    final_average = sum(list_of_averages)/len(list_of_averages)
    print(f'The average of all registered students is {final_average}')

