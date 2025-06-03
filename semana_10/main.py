
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
            actions.show_students()
        elif num_select == 3:
            actions.compare_avg()
        elif num_select == 4:
            print(f'Total Average for all students is {actions.show_average_of_avegares()}')
        elif num_select == 5:
            data.export2csv()
        elif num_select == 6:
            data.import_csv()
        elif num_select == 7:
            running = False
            print('Goodbye')
        else:
            print('not there yet')


main()