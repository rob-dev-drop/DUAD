#Pide al usuario ingresar 6 veces el valor de 1 o 2 para representar respectivamente una unidad de mujer o hombre y
#muestra el porcentaje de estos

hombre = 0
mujer = 0
contador = 0

while (contador < 6):
    dato = int(input('Ingrese 1 si la persona es mujer, 2 si la persona es hombre: '))
    if (dato >= 3 or dato <= 0):
        print("Ingrese un valor de 1 o 2")
    else:
        if (dato == 1):
            mujer += 1
            contador += 1
        else:
            hombre += 1
            contador += 1

porcentajeh = hombre/6 * 100
porcentajem = mujer/6 * 100

print(f'Hay un total de {int(porcentajem)}% de mujeres y un {int(porcentajeh)}% de hombres')