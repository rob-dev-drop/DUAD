#Cree un programa que use una lista para eliminar keys de un diccionario.

supermercado = {
    "queso" : 5000,
    "semillas" : 7500,
    "atun" : 2500,
    "tortillas" : 1500
}

hay_en_casa = ["tortillas", "atun"]

for index in hay_en_casa:
    supermercado.pop(index)
    
print(supermercado)