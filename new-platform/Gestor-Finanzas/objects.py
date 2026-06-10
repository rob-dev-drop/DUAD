
class Categoria:

    def __init__(self, nombre):
        self.nombre = nombre

class Movimiento:

    def __init__(self, descripcion,fecha,monto,categoria,tipo='Gasto'):
        self.descripcion = descripcion
        self.fecha = fecha
        self.monto = monto
        self.categoria = categoria
        self.tipo = tipo

    def list_data(self):
        x = []
        x.append(self.descripcion)
        x.append(self.fecha)
        x.append(int(self.monto))
        x.append(self.categoria.nombre)
        x.append(self.tipo)
        return x
    













