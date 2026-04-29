from product import Product

class SaleDetail:
    def __init__(self, detail_id=None, sale_id=None, product: Product=None, quantity=None):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        if product.stock < quantity:
            raise ValueError("Insufficient stock for the sale")

        self.detail_id = detail_id
        self.sale_id = sale_id
        self.product = product
        self.quantity = quantity
        self.unit_price = product.price
        self.subtotal = self.unit_price * quantity

    def __str__(self):
        return (f"Detail {self.detail_id}: Sale {self.sale_id}, "
                f"Product {self.product.name}, Quantity {self.quantity}, "
                f"Unit Price {self.unit_price}, Subtotal {self.subtotal}")


