#Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
#1. Suma
#2. Resta
#3. Multiplicación
#4. División
#5. Borrar resultado
#Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
#Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.


valor_actual = 0
running = True

def numero_ingresar():
    global valor_actual #Investigando, me di cuenta que uno puede llamar una variable global utilizando global antes de la variable para no crear una local con el mismo nombre
    if valor_actual == 0:
        try:
            valor_actual = int(input("Ingrese su primer numero: "))
        except ValueError:
            print('Valor no valido')
    else:
        print(f'Valor actual: {valor_actual}')
        

def sumar():
    numero_ingresar()
    global valor_actual
    try:
        num = int(input("ingrese el valor que desea sumar: "))
        valor_actual += num
    except ValueError:
        print('Valor no valido para sumar')
    
    


def restar():
    numero_ingresar()
    global valor_actual
    try:
        num = int(input("ingrese el valor que desea restar: "))
        valor_actual -= num
    except ValueError:
        print('Valor no valido para restar')

def multiplicar():
    numero_ingresar()
    global valor_actual
    try:
        num = int(input("ingrese el valor por el que desea multiplicar: "))
        valor_actual *= num
    except ValueError:
        print('Valor no valido para multiplicar')

def dividir():
    numero_ingresar()
    global valor_actual
    try:
        num = int(input("ingrese el valor por el que desea dividir: "))
        valor_actual /= num
    except ValueError:
        print('valor no valido para dividir')
    except ZeroDivisionError:
        print('No puedes dividir entre cero')

def borrar():
    global valor_actual
    valor_actual = 0
    print('Borrado!')
    

def menu_mostrar():
    print("Ingrese el numero de acuerdo a la operacion que desea hacer:")
    print("1 - Suma")
    print("2 - Resta")
    print("3 - Multiplicacion")
    print("4 - Division")
    print("5 - Borrar")
    print("6 - Salir")


def operacion_seleccionar():
    lrunning = True
    while lrunning == True:
        try:
            numero_ingresado = int(input("Ingrese su seleccion: "))
            if numero_ingresado > 0 and numero_ingresado < 7:
                lrunning = False
                return numero_ingresado
            else: 
                raise ValueError()
        except ValueError:
            print('Seleccion invalida, Guachin, escoje un numero de la lista')

def operacion_ejecutar(num):
    global running
    if num == 1:
        sumar()
    elif num == 2:
        restar()
    elif num == 3:
        multiplicar()
    elif num == 4:
        dividir()
    elif num == 5:
        borrar()
    elif num == 6:
        running = False
    print(f"Tu valor resultante es: {valor_actual}")
    

def main():
    global running
    while running == True:
        menu_mostrar()
        operacion_ejecutar(operacion_seleccionar())

main()


