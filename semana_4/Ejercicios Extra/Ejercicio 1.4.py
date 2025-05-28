#Pide al usuario 2 numeros y los muestra de menor a mayor, imprimiendo las mismas dos variables donde se ingresan los datos

primero = int(input('Ingrese el primer numero: '))
segundo = int(input('Ingrese el segundo numero: '))
if (primero > segundo):
    print(f'A: {primero}, B: {segundo}')
else:
    memoria = segundo
    segundo = primero
    primero = memoria
    print(f'A: {primero}, B: {segundo}')
