import actions


def show_menu():
    print('Choose an option:')
    print('1 - Add student')
    print('2 - Student list')
    print('3 - Show TOP 3 students')
    print('4 - Show score average for all students')
    print('5 - Export current information to CSV')
    print('6 - Import from CSV')
    selection = actions.choose_menu()
    return selection



