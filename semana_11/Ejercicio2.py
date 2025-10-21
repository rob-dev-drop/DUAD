#Ejercicio 2

class Person():
	def __init__(self, name):
		self.name = name
		self.age = 0

class Bus():
    def __init__(self):
        self.max_passengers = 5
        self.people_inside = []

    def add_person(self, new_passenger):
        if len(self.people_inside) < self.max_passengers:
            self.people_inside.append(new_passenger)
            print(f"{new_passenger.name} entered the bus")
        else:
            print(f"The bus is full, {new_passenger.name} couldn't get in")

    def last_stop(self,x):
        if self.people_inside:
            person_out = self.people_inside[x]
            print(f"{person_out.name} got out the bus")
            return person_out
        else:
            print("Bus is empty")


person_1 = Person("Jotaro")
person_2 = Person("Giorno")
person_3 = Person("Johnathan")
person_4 = Person("Joseph")
person_5 = Person("Josuke")
person_6 = Person("Jolyne")
bus_1 = Bus()

bus_1.add_person(person_1)
bus_1.add_person(person_2)
bus_1.add_person(person_3)
bus_1.add_person(person_4)
bus_1.add_person(person_5)
bus_1.add_person(person_6)

for item in range(len(bus_1.people_inside)):
    bus_1.last_stop(item)