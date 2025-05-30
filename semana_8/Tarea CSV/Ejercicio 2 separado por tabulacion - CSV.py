#  Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.
    ##Debe incluir:
        ###Nombre
        ###Género
        ###Desarrollador
        ###Clasificación ESRB

import csv

lista_videojuegos = [{'nombre':'mario', 'genero':'plataforma', 'desarrollador':'nintendo', 'clasificacion':'E'}]

def ingresar_datos():
    data_name = input("Introduce el nombre del videojuego: ")
    data_genre = input("Introduce el genero del videojuego: ")
    data_dev = input("Introduce el desarrollador del videojuego: ")
    data_esrb = input("Introduce la clasificacion del videojuego: ")
    diccionario = {
        'nombre':'placeholder',
        'genero':'placeholder',
        'desarrollador':'placeholder',
        'clasificacion':'placeholder'
    }
    diccionario['nombre'] = data_name
    diccionario['genero'] =data_genre
    diccionario['desarrollador'] = data_dev
    diccionario['clasificacion'] =data_esrb
    return diccionario


def agregar_juego(game):
    global lista_videojuegos
    lista_videojuegos.append(game)


def eliminar_juego():
    global lista_videojuegos
    if len(lista_videojuegos) == 0:
        print('No hay juegos aun')
    else:
        print('Estos son los juegos ingresados hasta ahora: ')
        for index, game in enumerate(lista_videojuegos):
            juego = game.get('nombre')
            print(f'Indice: {index} - {juego}')
        print('Cual juego desea borrar?')
        try:
            killgame = int(input('Introduzca el numero del indice'))
            if killgame > len(lista_videojuegos) or killgame < 0:
                raise IndexError
            else:
                soontokill = lista_videojuegos[killgame]
                print(f'El juego {soontokill.get('nombre')} ha sido eliminado')
                lista_videojuegos.pop(killgame)
        except ValueError:
            print('Elije un numero de la lista, no una letra')
        except IndexError:
            print('Elije un numero de la lista')


def exportar_csv():
    global lista_videojuegos
    nombre_archivo = input('Elija el nombre del archivo que desea para su CSV: ')
    def write_csv_file(file_path, data, headers):
        with open(file_path, 'w', encoding='utf-8') as file:
            writer = csv.DictWriter(file, headers, dialect='excel-tab')
            writer.writeheader()
            writer.writerows(data)
    write_csv_file(f'{nombre_archivo}.csv', lista_videojuegos, lista_videojuegos[0].keys())


def menu():
    print('Elija una opcion:')
    print('1 - Agregar un juego')
    print('2 - Eliminar un juego')
    print('3 - Exportar a CSV')
    print('4 - Salir')
    print('')
    selection = menu_seleccionar()
    return selection

def menu_seleccionar():
    lrunning = True
    while lrunning == True:
        try:
            numero_ingresado = int(input("Ingrese su seleccion: "))
            if numero_ingresado > 0 and numero_ingresado < 5:
                lrunning = False
                return numero_ingresado
            else: 
                raise ValueError()
        except ValueError:
            print('Seleccion invalida, rufian, escoje un numero de la opciones')

def main():
    global lista_videojuegos
    print('Bienvenido, este programa agrega la cantidad que quieras de juegos y sus caracteristicas en un archivo CSV')
    running = True
    while running == True:
        nextstep = menu()
        if nextstep == 1:
            agregar_juego(ingresar_datos())
        elif nextstep == 2:
            eliminar_juego()
        elif nextstep == 3:
            exportar_csv()
            continuar = input('Desea crear otro archivo desde cero? (y/n) ')
            if continuar == 'y':
                lista_videojuegos = []
            elif continuar == 'n':
                print('Hasta Luego')
                running = False
        elif nextstep == 4:
            print('Hasta Luego')
            running = False


main()




