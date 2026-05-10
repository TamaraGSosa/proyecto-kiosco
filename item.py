from product import Product

class Item:
    def __init__(self, product: Product, quantity: int):
        if quantity <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        if product.stock < quantity:
            raise ValueError("Stock insuficiente para la venta")
        
        self.product = product
        self.quantity = quantity

    @property
    def quantity(self):
        return self._quantity
    
    
    @quantity.setter
    def quantity(self, new_quantity):
        self._quantity = new_quantity
        
    def __str__(self):
        return f"Producto: {self.product.name}, Cantidad: {self.quantity}, Subtotal: {self.subtotal}"
    
    @property
    def subtotal(self):
        return self.product.price * self.quantity