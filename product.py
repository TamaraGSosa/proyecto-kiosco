class Product:
    # Se agrega id_producto=None para que el ID sea opcional
    def __init__(self, name, price, stock, id_producto=None):
        self.id_producto = id_producto 
        self.name = name
        self.price = price
        self.stock = stock

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not new_name:
            raise ValueError("El nombre no puede estar vacio")
        self._name = new_name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("El precio no puede ser negativo")
        self._price = new_price

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, new_stock):
        if new_stock < 0:
            raise ValueError("El stock no puede ser negativo")
        self._stock = new_stock

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }