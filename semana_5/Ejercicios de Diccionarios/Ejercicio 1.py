hotels = {

}

hotel_name = str(input('Ingrese el nombre del hotel: '))
hotel_stars = int(input('Ingrese el numero de estrellas que tiene: '))
number = int(input("Ingrese el numero de habitacion: "))
floor = int(input("Ingrese el piso: "))
price = int(input("Ingrese el precio por noche"))

hotel_rooms = [f"Habitacion numero: {number}", f"Piso: {floor}", f"Precio por noche {price}"]

hotels['hotel'] = hotel_name
hotels['estrellas'] = hotel_stars
hotels['habitacion'] = hotel_rooms

print(hotels)

#Cree un diccionario que guarde la siguiente información sobre un hotel