def sumar_numeros(var1,var2):
    suma = var1 + var2
    print('Este texto esta imprimiendose desde la primera funcion, se muestra hasta que la segunda funcion la llama, justo despues de mostrar el texto que pide los valores que esta funcion suma')
    return suma

def ingresar_numeros():
    num1 = int(input('Ingrese el primer numero: '))
    num2 = int(input('Ingrese el segundo numero: '))
    print(f'Este texto se imprime desde la segunda funcion y el resultado de sumar estos dos numeros es: {sumar_numeros(num1,num2)}')
    
ingresar_numeros()