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

            elif event == 'agregar': #aqui es donde se hace la validacion, pero el ciclo no deberia cerrarse
                if util.number_validation(values['-Mon-']) == True:
                    try:
                        x = ob.Movimiento(values['-Des-'],values['-Fec-'],values['-Mon-'],ob.Categoria(values['-Cat-']),tipo)
                        add_item_window.close()
                        return x
                    except AttributeError:
                        add_item_window.close()
                        return AttributeError
                else:
                    sg.popup('Monto Ingresado no es numerico. Ingrese un numero')
                    add_item_window.close()
                    return 0

            elif event == 'cerrar':
                add_item_window.close()
                return 0


def show_add_cat_window(): 
    
    category_list = fl.read_categories(fl.import_json("save_data.json")["categorias"])

    column1 = [[sg.Table(category_list, headings=["Categorias"],key='-MOV_TABLEs-',hide_vertical_scroll=True)]]
    column2 = [[sg.Text("Nueva Categoria"),sg.Input(key='-NEW_CAT-')],[sg.Button('Agregar')]]

    layout = [[sg.Column(column1, element_justification='Left'), sg.Column(column2, element_justification='right')]]

    window = sg.Window("Add a cat", layout)
    while True:
            event, values = window.read()
            
            if event == sg.WIN_CLOSED:
                break
            elif event == 'Agregar': 
                new_cat = ob.Categoria(values['-NEW_CAT-'])
                window.close()
                return new_cat
    


def show_main_window():

    main_category_list = fl.read_categories(fl.import_json("save_data.json")["categorias"])
    frontend_movement_table = fl.dict_to_list(fl.import_json("save_data.json")["movimientos"])
    backend_movement_table = fl.create_obj_list(fl.import_json("save_data.json")["movimientos"])


    def save_current_state():
        fl.export_json(backend_movement_table)


    def update_ui(key,target_element):
        window[key].update(values=target_element)


    def add_item(tipo='Gasto'):
        try:
            x = show_add_item_window(main_category_list,tipo)
            if x != 0:
                backend_movement_table.append(x)
                frontend_movement_table.append(x.list_data())
                update_ui('-MOV_TABLE-',frontend_movement_table)
            else:
                return
            
        except (AttributeError):
            sg.popup("Nueva entrada ha sido descartada")
        except ValueError:
            sg.popup("El monto debe ser un valor numerico positivo")
        save_current_state()


    def add_cat():
        try:
            new_category = show_add_cat_window()
            main_category_list.append(new_category.nombre)
        except AttributeError:
            sg.popup("Nueva categoria descartada")

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
            save_current_state()
            break
        elif event == "-CAT_BTN-":
            add_cat()

        elif event == "-SPEND_BTN-":
            add_item()

        elif event == "-INC_BTN-":
            add_item('Ingreso')

        elif event == "-EXP_BTN-":
            fl.export_csv(backend_movement_table)

    window.close()

if __name__ == "__main__":
    show_main_window()

