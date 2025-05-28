#Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente
#adulto joven, adulto, o adulto mayor.

nombre = str(input('Ingrese nombre: '))
apellido = str(input('Ingrese apellido: '))
edad = int(input('Ingrese edad: '))
pob = ["bebé", "niño", "preadolescente", "adolescente", "adulto joven", "adulto", "adulto mayor"]

if (edad < 3 and edad >= 0):
    print(f'{nombre} {apellido} es un {pob[0]}')
elif (edad < 10):
    print(f'{nombre} {apellido} es un {pob[1]}')
elif (edad < 12):
    print(f'{nombre} {apellido} es un {pob[2]}')
elif (edad < 19):
    print(f'{nombre} {apellido} es un {pob[3]}')
elif (edad < 35):
    print(f'{nombre} {apellido} es un {pob[4]}')
elif (edad < 59):
    print(f'{nombre} {apellido} es un {pob[5]}')
else:
    print(f'{nombre} {apellido} es un {pob[6]}')