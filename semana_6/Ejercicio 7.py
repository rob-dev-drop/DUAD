#7.Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma

def insert_number():
    number_count = int(input("Cuantos numeros desea agregar? "))
    return number_count


def list_build():
    total_numbers = insert_number()
    counter = 1
    lista = []
    while counter <= total_numbers:
        num = int(input(f'Ingrese un numero (van {counter} de {total_numbers})'))
        lista.append(num)
        counter += 1
    return lista


def determinar_factorial(numero):
    factorial = 1
    for index in range(1,numero+1):
        factorial *= index
    return factorial


def sacar_primos(parameter):
    prime = 0
    if (determinar_factorial(parameter-1)+1) % parameter == 0:
        prime = parameter
        return prime
    else:
        return 0


def todojunto():
    lista_primos = []
    lista_no_primos = []
    lista = list_build()
    for num in lista:
        if sacar_primos(num) == 0:
            lista_no_primos.append(num)
        else:
            primenum = sacar_primos(num)
            lista_primos.append(primenum)
    return lista_primos

print(todojunto())














