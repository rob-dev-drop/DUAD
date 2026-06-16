# Aqui voy a poner la logica de leer y escribir los CSV
import csv
import json
import objects as ob


#========= Importing Logic =========#


#lee el file json en disco y retorna unu diccionario con dos keys: categorias y movimientos
def import_json(savefile):
    data = {
        "categorias": [],
        "movimientos": []
    }
    try:
        with open(savefile, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return data
        


#Accesa la lista de diccionarios en el key "movimientos" del file json guardado, crea los objetos 'de fondo'
def create_obj_list(list_of_dictionaries): 
    object_list = []
    for i, row in enumerate(list_of_dictionaries):
        movimiento = list_of_dictionaries[i]["descripcion"]
        fecha = list_of_dictionaries[i]["fecha"]
        monto = float(list_of_dictionaries[i]["monto"])
        categoria = ob.Categoria(list_of_dictionaries[i]["categoria"])
        tipo = list_of_dictionaries[i]["tipo"]
        x = ob.Movimiento(movimiento,fecha,monto,categoria,tipo)
        object_list.append(x)
    return object_list

#print(create_obj_list(import_json()["movimientos"]))

#Accesa "movimientos" del file json guardado, crea la lista de listas para mostrarse en la interfaz
def dict_to_list(list_of_dictionaries):  
    outer_list = []
    
    for i, row in enumerate(list_of_dictionaries):
        inner_list = []
        movimiento = list_of_dictionaries[i]["descripcion"]
        fecha = list_of_dictionaries[i]["fecha"]
        monto = float(list_of_dictionaries[i]["monto"])
        categoria = list_of_dictionaries[i]["categoria"]
        tipo = list_of_dictionaries[i]["tipo"]
        inner_list.append(movimiento)
        inner_list.append(fecha)
        inner_list.append(monto)
        inner_list.append(categoria)
        inner_list.append(tipo)
        outer_list.append(inner_list)
    return outer_list

#print(dict_to_list(import_json()["movimientos"]))

def read_categories(list_of_categories):
    category_list = []
    for i in list_of_categories:
        if i not in category_list:
            category_list.append(i)
    return category_list

#read_categories(import_json()["categorias"])


#========= Exporting Logic =========#

#======= Exporting JSON Logic =====#

#Convierte la lista de onjetos en el formato en el que se escribira en json, un diccionario
def convert_objects_to_json_format(movement_list, category_list):
    final_dict = {
        "categorias": [],
        "movimientos": []
    }

    for i in movement_list:
        temp_dict = {
            "descripcion": "",
            "fecha": "",
            "monto": 0,
            "categoria": "",
            "tipo": ""
        }

        if i.categoria.nombre not in final_dict["categorias"]:
            final_dict["categorias"].append(i.categoria.nombre)
        
        temp_dict["descripcion"] = i.descripcion
        temp_dict["fecha"] = i.fecha
        temp_dict["monto"] = i.monto
        temp_dict["categoria"] = i.categoria.nombre
        temp_dict["tipo"] = i.tipo
        final_dict["movimientos"].append(temp_dict)

    for i in category_list:
        if i not in final_dict["categorias"]:
            final_dict["categorias"].append(i)

    return final_dict


#Exporta el diccionario a su respectivo file JSON, ya viene con su formato gracias a convert_object_to_json_format()
def export_json(movement_list, category_list): #tengo que convertir la lista de objetos en una lista de diccionarios
    with open("save_data.json", "w",encoding='utf-8') as file:
        json.dump(convert_objects_to_json_format(movement_list, category_list), file, indent=4)


#======= Exporting CSV Logic =====#

def convert_obj_to_dictionary(object_list):
    lista_a_exportar = []

    for i in object_list:                        #esto creo que deberia ser su propio metodo. Ya que convierte los objetos en diccionarios
        temp_dic = {"Descripcion":None,
                    "Fecha":None,
                    "Monto":None,
                    "Categoria":None,
                    "Tipo":True}
        temp_dic["Descripcion"] = i.descripcion
        temp_dic["Fecha"] = i.fecha
        temp_dic["Monto"] = i.monto
        temp_dic["Categoria"] = i.categoria.nombre
        temp_dic["Tipo"] = i.tipo
        lista_a_exportar.append(temp_dic)
    return lista_a_exportar


def export_csv(object_list): 
    headers = ['Descripcion', 'Fecha', 'Monto', 'Categoria', 'Tipo']
    with open('export.csv', mode='w', newline='', encoding='utf-8') as file: #mode W para escribir file
        writer = csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(convert_obj_to_dictionary(object_list)) #Alertas de confirmacion o fallo tienen que ser incluidas en el programa









