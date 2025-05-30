tiempo = int(input('Introduzca el tiempo en segundos: '))
seg_faltantes = 0
if (tiempo > 600):
    print('Mayor')
else:
    seg_faltantes = 600 - tiempo
    print(f'Para llegar a 10 minutos hacen falta {seg_faltantes} segundos')
