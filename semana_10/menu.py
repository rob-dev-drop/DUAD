import actions
import data

def show_menu(): #Prints the menu options
    print('Choose an option:')
    print('1 - Add student')
    print('2 - Student list')
    print('3 - Show TOP 3 students')
    print('4 - Show score average for all students')
    print('5 - Export current information to CSV')
    print('6 - Import from CSV')
    print('7 - Exit')
    selection = choose_menu()
    return selection


def choose_menu(): #validates the menu options
    lrunning = True
    while lrunning == True:
        try:
            input_num = int(input("Input your choice: "))
            if input_num  > 0 and input_num  <= 7:
                lrunning = False
                return input_num 
            else: 
                raise ValueError()
        except ValueError:
            print('Invalid selection, please select an option from the menu')


def trigger_main_menu(): #has logic to call fuctions from actions module according to the option selected in show_menu()
    running = True
    x = []
    while running == True:
        num_select = show_menu()
        if num_select == 1:
            x.append(actions.add_student())
        elif num_select == 2:
            actions.show_students(x)
        elif num_select == 3:
            actions.compare_avg(x)
        elif num_select == 4:
            actions.show_average_of_avegares(x)
        elif num_select == 5:
            data.export2csv(x)
        elif num_select == 6:
            x = data.import_csv()
        elif num_select == 7:
            running = False
            print('Goodbye')
        else:
            print('not there yet')



