#Ejercicios de semana 11

#Ejercicio 1

class Circle:
    radius = 1
    def get_area(self, r):
        area = (r * r) * 3.14159
        return area

my_circle = Circle()

print(my_circle.radius)
print(my_circle.get_area(50))