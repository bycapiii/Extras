
class Producto:
    
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def actualizar_precio(self, cambio_porcentaje, está_elevado ):
        if está_elevado==True :
            self.precio *+cambio_porcentaje
        else:
            self.precio *-cambio_porcentaje
        return self
    
    def print_info(self):
        print(f"Este es un producto {self.nombre} {self.precio} {self.categoria} ")


