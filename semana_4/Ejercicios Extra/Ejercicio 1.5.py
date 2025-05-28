#Pide la velociadad en km/h y la conviente a m/s
km = int(input('Ingrese la velocidad en km/h: '))
metros = km * 1000
mps = metros/3600
print(f'La velocidad en m/s es de {int(mps)}')