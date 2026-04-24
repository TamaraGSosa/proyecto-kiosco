from datetime import datetime
class Venta:
    def __init__(self,nombre_producto,total,fecha=None):
        if total <0:
            raise ValueError("El total no puede ser negativo")
        self.nombre_producto=nombre_producto
        self.total=total
        self.fecha= fecha if fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def __str__(self):
        return f"Nombre:{self.nombre_producto} - Total ${self.total} - Fecha {self.fecha}"


venta1=Venta("cartuchera",10)

print(venta1)