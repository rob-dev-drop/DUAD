# Cree un programa que permita agregar un Pokémon nuevo al archivo previamente dado.

import json

pokedex = []

def json_abrir():
    global pokedex
    with open('pokemon.json','r') as file:
        pokedex = json.load(file)


def ingresar_datos():
    data_name = input("Introduce el nombre del pokemon: ")
    data_type = input("Introduce el tipo: ")
    data_stat_hp = int(input("Introduce los puntos de vida: "))
    data_stat_defense = int(input("Introduce los puntos de defensa: "))
    data_stat_attck = int(input("Introduce los puntos de ataque: "))
    data_stat_spattack = int(input("Introduce los puntos de ataque especial: "))
    data_stat_spdefense = int(input("Introduce los puntos de defensa especial: "))
    data_stat_speed = int(input("Introduce la velocidad: "))
    
    diccionario = {
        'name':{},
        'type':[],
        'base':{
                    "HP": 999,
                    "Attack": 999,
                    "Defense": 999,
                    "Sp. Attack": 999,
                    "Sp. Defense": 999,
                    "Speed": 999
        }
    }
    diccionario['name'] = {'english':data_name}
    diccionario["type"] = [data_type]
    diccionario["base"] = {
        "HP": data_stat_hp,
        "Attack": data_stat_attck,
        "Defense": data_stat_defense,
        "Sp. Attack": data_stat_spattack,
        "Sp. Defense": data_stat_spdefense,
        "Speed": data_stat_speed
    }
    return diccionario


def add_pokemon():
    global pokedex
    pokedex.append(ingresar_datos())


def show_pokemon():
    global pokedex
    print('Estos son los pokemon en la Pokedex:')
    for num, pokemon in enumerate(pokedex):
        index = pokemon
        index2 = index.get('name')
        print(f'{num} - {index2.get('english')}')
    print('')
    input('presione Enter para continuar')


def delete_pokemon():
    global pokedex
    show_pokemon()
    print('para borrar, ingrese el indice del pokemon que desea borrar')
    try:
        pokedelete = int(input())
        if pokedelete >= 0 or pokedelete < (len(pokedex)-1):
            pokedex.pop(pokedelete)
            print('Borrado')
        else:
            raise ValueError
    except ValueError:
        print('Ingrese un numero de los indices mostrados')
    except IndexError:
        print('Ingrese un numero de los indices mostrados')



def export_pokemon():
    global pokedex
    with open('pokemon.json', 'w') as file:
        json.dump(pokedex, file, indent=4)
    print('Pokedex guardado satisfactoriamente')
    print('')


def menu():
    print('1 - ingresar nuevo pokemon')
    print('2 - Guardar pokedex(guardar en pokemon.JSON)')
    print('3 - Mostrar pokemon en pokedex')
    print('4 - Borrar pokemon')
    print('5 - Salir')
    print('')
    print('Que desea hacer?' )


def menu_choose():
        choice_selected = False
        while choice_selected == False:
            try:
                seleccion = int(input())
                if seleccion < 0 or seleccion > 5:
                    raise ValueError
                else:
                    choice_selected = True
                    return seleccion
            except ValueError:
                print('Eleccion no valida, intente de nuevo')


def main():
    prunning = True
    json_abrir()
    while prunning == True:
        menu()
        nextstep = menu_choose()
        if nextstep == 1:
            add_pokemon()
        elif nextstep == 2:
            export_pokemon()
        elif nextstep == 3:
            show_pokemon()
        elif nextstep == 4:
            delete_pokemon()
        elif nextstep == 5:
            print("Hasta Luego")
            prunning = False


main()
