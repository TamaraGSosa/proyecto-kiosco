from product import Product

class Item:
    def __init__(self, product: Product, quantity: int):
        if quantity <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        if product.stock < quantity:
            raise ValueError("Stock insuficiente para la venta")

        self.product = product
        self.quantity = quantity
        self.unit_price = product.price
        self.subtotal = self.unit_price * quantity

    def __str__(self):
        return (f"Producto: {self.product.name}, "
                f"Cantidad: {self.quantity}, "
                f"Precio unitario: {self.unit_price}, "
                f"Subtotal: {self.subtotal}")
