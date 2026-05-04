from datetime import datetime
from product import Product
from item import Item
class Sell:
    def __init__(self):
        
        self.date= dt.datetime.now().isoformat()
        self._item=[]

    @property
    def total(self):
        new_total=0
        for item in self._items:
            new_total+=item.subtotal
        return new_total
    @property
    def add_items(self,product: Product,quantity):
        self._items.append(Item(product,quantity))
        

    def to_dic(self):
        return{
            "total":self.total,
            "date":self._date
        }
