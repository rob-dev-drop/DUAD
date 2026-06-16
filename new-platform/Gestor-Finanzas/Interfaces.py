import FreeSimpleGUI as sg
import File_logic as fl
import objects as ob
import utilities as util



def show_add_item_window(category_list,tipo="Gasto"): 
    
    layout = [[sg.Text('Descripcion')],[sg.Input(key='-Des-')],
            [sg.Text('Fecha')],[sg.Input(key='-Fec-')],
            [sg.Text('Monto')],[sg.Input(key='-Mon-')],
            [sg.Text('Categoria')],[sg.Combo(category_list, default_value='',readonly = False, key='-Cat-')],
            [sg.Button('agregar'),sg.Button('cerrar')]
    ]


    add_item_window = sg.Window("Add a expense", layout)
    while True:
            event, values = add_item_window.read()
            
            if event == sg.WIN_CLOSED:
                return 0

            elif event == 'agregar': 
                try:
                    new_object = util.GestorFinanzas.create_movement(values['-Des-'],values['-Fec-'],values['-Mon-'],values['-Cat-'],category_list,tipo)
                    add_item_window.close()
                    return new_object
                except AttributeError:
                    sg.popup("Debe llenar todos los espacios requeridos")
                except ValueError:
                    sg.popup("Monto invalido. Ingresa un numero")
            
            elif event == 'cerrar':
                add_item_window.close()
                return 'cancel'


def show_add_cat_window(main_category_list): 
    
    category_list = main_category_list

    column1 = [[sg.Table(category_list, headings=["Categorias"],key='-MOV_TABLEs-',hide_vertical_scroll=True)]]
    column2 = [[sg.Text("Nueva Categoria"),sg.Input(key='-NEW_CAT-')],[sg.Button('Agregar')]]

    layout = [[sg.Column(column1, element_justification='Left'), sg.Column(column2, element_justification='right')]]

    window = sg.Window("Add a cat", layout)
    while True:
            event, values = window.read()
            
            if event == sg.WIN_CLOSED:
                break
            elif event == 'Agregar': 
                try:
                    new_category = util.GestorFinanzas.create_category(values['-NEW_CAT-'],category_list)
                    category_list.append(new_category.nombre)
                    window.close()
                    return category_list
                except NameError:
                    sg.popup("La categoria ya existe")
                    window.close()
                except AttributeError:
                    sg.popup("Ingrese el nombre de la categoria")
    


def show_main_window():

    main_category_list, frontend_movement_table, backend_movement_table = util.GestorFinanzas.load_start_up()


    def update_ui(key,target_element):
        window[key].update(values=target_element)


    layout = [
        [sg.Text("Bienvenido al gestor de finanzas",key='-TITLE-')],
        [sg.Button('Agregar Categoria',key='-CAT_BTN-'), sg.Button('Agregar Gasto',key='-SPEND_BTN-'),
        sg.Button('Agregar Ingreso',key='-INC_BTN-'), sg.Button('Export CSV',key='-EXP_BTN-')],
        [[sg.Table(frontend_movement_table, headings=["Descripcion", "Fecha", "Monto", "Categoria","Tipo"],key='-MOV_TABLE-',hide_vertical_scroll=True)]]
        ]
    
    window = sg.Window("Gestor de Finanzas", layout)

    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED:
            util.GestorFinanzas.save_current_state(backend_movement_table,main_category_list)
            break
        elif event == "-CAT_BTN-":
            show_add_cat_window(main_category_list)

        elif event == "-SPEND_BTN-":
            if util.GestorFinanzas.check_for_categories(main_category_list) == True:
                x = show_add_item_window(main_category_list)
                util.GestorFinanzas.update_tables(frontend_movement_table,backend_movement_table,x)
                update_ui('-MOV_TABLE-',frontend_movement_table)
            else:
                sg.popup("Aun no hay categorias, agrega una categoria primero!")

        elif event == "-INC_BTN-":
            if util.GestorFinanzas.check_for_categories(main_category_list) == True:
                x = show_add_item_window(main_category_list,'ingreso')
                util.GestorFinanzas.update_tables(frontend_movement_table,backend_movement_table,x)
                update_ui('-MOV_TABLE-',frontend_movement_table)
            else:
                sg.popup("Aun no hay categorias, agrega una categoria primero!")

        elif event == "-EXP_BTN-":
            fl.export_csv(backend_movement_table)

    window.close()

if __name__ == "__main__":
    show_main_window()

