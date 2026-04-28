class Producto:
    def __init__(self,id_producto,name,price,stock):
        if price<0:
            raise ValueError ("El precio no puede ser negativo")
        if stock <0:
            raise ValueError ("El stock no puede ser negativo")
        self.name=name
        self.price=price
        self.stock=stock
        self.id_producto=id_producto

    def set_price(self, new_price):
        if new_price <0:
            raise ValueError ("El precio no puede ser negativo")
        self.price=new_price

    def  set_stock(self,new_stock):
        if new_stock <0:
            raise ValueError ("El stock no puede ser negativo")
        self.stock=new_stock

# diccionario por si implementamos json        
#    def to_dict(self):
#        return{
#            "name":self.name,
#            "price":self.price,
#            "stock":self.stock
#        }

    def __str__(self):
        return f"id:{self.id_producto}-Nombre:{self.name}-Precio:{self.price} ({self.stock} existe en stock)"

cartuchera=Producto(1,"cartuchera",50000,10)
carpeta=Producto(2,"carpeta",70000,10)

inventario=[cartuchera,carpeta]

for i in inventario:
    print(i)
