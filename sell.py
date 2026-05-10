from datetime import datetime
from product import Product
from item import Item

class Sell:
    def __init__(self , sell_id=None):
        self.sell_id = sell_id
        self.date = datetime.now().isoformat()
        self._items = []

    @property
    def total(self):
        new_total = 0
        for item in self._items:
            new_total += item.subtotal
        return new_total

    @property
    def items(self):
        return self._items
    
    def add_item(self, product: Product, quantity: int):
        self._items.append(Item(product, quantity))

    def to_dict(self):
        return {
            "total": self.total,
            "fecha": self.date
        }