#5. Dada `n` cantidad de notas de un estudiante, calcular:
#   1. Cuantas notas tiene aprobadas (mayor a 70).
#    2. Cuantas notas tiene desaprobadas (menor a 70).
#    3. El promedio de todas.
#    4. El promedio de las aprobadas.
#    5. El promedio de las desaprobadas.

t_notas = int(input('Ingrese la cantidad de notas: '))
c_notas = 1
notas_a = 0
notas_r = 0
prom_a = 0
prom_r = 0
prom_t = 0
while (c_notas <= t_notas):
    nota = int(input(f'Ingrese la nota numero {c_notas}: '))
    if (nota < 70):
        notas_r += 1
        prom_r += nota
        c_notas += 1
    else:
        notas_a += 1
        prom_a += nota
        c_notas += 1
    prom_t = prom_t + (nota / t_notas)

prom_a /= notas_a
prom_r /= notas_r

print(f'El estudiante tiene {int(notas_a)} notas aprobadas')
print(f'El promedio de notas aprobadas es de {int(prom_a)}')
print(f'El estudiante tiene {int(notas_r)} notas reprobadas')
print(f'El promedio de notas reprobadas es de {int(prom_r)}')
print(f'Este es el promedio total {int(prom_t)}')