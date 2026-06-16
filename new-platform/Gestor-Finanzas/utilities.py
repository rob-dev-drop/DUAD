import objects as ob
import File_logic as fl


class GestorFinanzas:
    
    @staticmethod
    def number_validation(num):
        if num >= 0:
            return num
        else:
            raise ValueError
    
    
    @staticmethod
    def check_for_categories(cat_list):
        if cat_list == []:
            return False
        else:
            return True
    
    
    @staticmethod
    def update_tables(ui_table, obj_table, obj):
        if obj == 'cancel':
            pass
        else:
            obj_table.append(obj)
            ui_table.append(obj.list_data())


    @staticmethod
    def check_available_categories(list,category):
        if category not in list:
            raise AttributeError
        else: 
            pass
    

    @staticmethod
    def create_movement(descripcion,fecha,monto,categoria,lista_categorias,tipo="gasto"):
        GestorFinanzas.check_available_categories(lista_categorias,categoria)
        if descripcion == '' or fecha == '' or categoria == '':
            raise AttributeError
        else:
            new_object = ob.Movimiento(descripcion,fecha,GestorFinanzas.number_validation(float(monto)),ob.Categoria(categoria),tipo)
            return new_object
            


    @staticmethod
    def create_category(nombre,category_list):
        x = category_list
        if nombre == "":
            raise AttributeError
        else:
            if nombre not in category_list:
                new_category = ob.Categoria(nombre)
                return new_category
            else:
                raise NameError


    @staticmethod
    def save_current_state(mov_list,cat_list):
        fl.export_json(mov_list,cat_list)
        return
    

    @staticmethod
    def load_start_up():
            main_category_list = fl.read_categories(fl.import_json("save_data.json")["categorias"])
            frontend_movement_table = fl.dict_to_list(fl.import_json("save_data.json")["movimientos"])
            backend_movement_table = fl.create_obj_list(fl.import_json("save_data.json")["movimientos"])
            return main_category_list, frontend_movement_table, backend_movement_table


