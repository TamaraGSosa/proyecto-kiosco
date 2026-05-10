from product import Product


class SellDetail:
    def __init__(self, detail_id=None, sell_id=None, product: Product | None = None, quantity: int | None = None):
        if product is None:
            raise ValueError("product es requerido")
        if quantity is None:
            raise ValueError("quantity es requerido")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        if product.stock < quantity:
            raise ValueError("Insufficient stock for the sale")

        self.detail_id = detail_id
        self.sell_id = sell_id
        self.product = product
        self.quantity = quantity
        self.unit_price = product.price
        self.subtotal = self.unit_price * quantity

    def __str__(self):
        return (
            f"Detail {self.detail_id}: Sell {self.sell_id}, "
            f"product {self.product.name}, Quantity {self.quantity}, "
            f"Unit Price {self.unit_price}, Subtotal {self.subtotal}"
        )



