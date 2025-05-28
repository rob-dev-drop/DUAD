# Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

lista_canciones = []

def read_file(path): #Funcion para leer el archivo que contiene los nombres de canciones del album Hypnotize de System of a Down
    with open(path) as file:
        for line in file.readlines(): #readlines() retorna una lista de lineas del archivo especificado.
            lista_canciones.append(line)




def write_file(path): #Funcion para escribir un archivo nuevo
    with open(path,'w') as file: #primero crea un archivo.txt con el nombre que se le de al parametro path
        file.write('Lista de canciones ordenadas alfabeticamente\n') #el archivo inicial crea un titulo con un break para que el siguiente codigo empiece a escribir desde la linea 2 del archivo
    with open(path,'a') as file:
        for a in sorted(lista_canciones): #El for itera por cada elemento de la lista en orden alfabetico y
            file.write(a)                 #lo agrega al archivo previamente creado


read_file('soadsongs.txt')
write_file('newsoad.txt')


