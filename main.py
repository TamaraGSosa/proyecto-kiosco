from product import Product
from product_repository import ProductRepository
from sell_item import SaleDetail   
from sell import Sell
from sell_repository import SellRepository

def main():
    # Inicializar repositorios
    product_repo = ProductRepository()
    product_repo.create_table()

    sell_repo = SellRepository()
    sell_repo.create_table()

    while True:
        print("\n--- Menú del Kiosco ---")
        print("1. Alta de producto")
        print("2. Listar productos")
        print("3. Realizar venta")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio: "))
                stock = int(input("Stock inicial: "))
                producto = Product(nombre, precio, stock)
                # Falta implementar insertar en ProductRepository
                # Ejemplo: product_repo.insertar_producto(producto)
                print(f"Producto {producto.name} agregado correctamente.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            try:
                productos = product_repo.listar_productos()  # Método a implementar
                for p in productos:
                    print(f"{p.name} - ${p.price} - Stock: {p.stock}")
            except Exception as e:
                print(f"Error al listar productos: {e}")

        elif opcion == "3":
            try:
                venta = Sell()

                productos = product_repo.listar_productos()
                for idx, p in enumerate(productos, start=1):
                    print(f"{idx}. {p.name} - ${p.price} - Stock: {p.stock}")

                seleccion = int(input("Seleccione producto: "))
                cantidad = int(input("Cantidad: "))
                producto = productos[seleccion - 1]

                # Crear detalle de venta
                detalle = SaleDetail(detail_id=1, sale_id=1, product=producto, quantity=cantidad)
                venta.add_item(producto, cantidad)

                print("Detalle de venta:")
                print(detalle)
                print(f"Total de la venta: ${venta.total}")

                # Guardar venta en la base de datos
                # Ejemplo: sell_repo.insertar_venta(venta)
            except ValueError as e:
                print(f"Error en la venta: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    main()
