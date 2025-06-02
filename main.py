
import menu
import actions
import data


def main():
    running = True
    while running == True:
        num_select = menu.show_menu()
        if num_select == 1:
            actions.add_student()
        elif num_select == 2:
            print(data.students_and_grades)
        elif num_select == 3:
            actions.compare_avg()
        else:
            print('not there yet')


main()