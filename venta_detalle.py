class VentaDetalle:
    def __init__(self, id_detalle, id_venta, id_producto, cantidad, precio_unitario):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        if precio_unitario < 0:
            raise ValueError("El precio no puede ser negativo")

        self.id_detalle = id_detalle
        self.id_venta = id_venta
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = precio_unitario * cantidad

    def __str__(self):
        return f"Detalle {self.id_detalle}: Venta {self.id_venta}, Producto {self.id_producto}, Cantidad {self.cantidad}, Precio {self.precio_unitario}, Subtotal {self.subtotal}"

detalle = VentaDetalle(1, 1, 1, 10, 50000)
print(detalle)
