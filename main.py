# proyecto Kiosco

from datetime import datetime

from product import Product
from product_repository import ProductRepository

from sell import Sell
from sell_repository import SellRepository

from sell_item_repository import SellItemRepository


product_repo = ProductRepository()
sale_repo = SellRepository()
sell_item_repo = SellItemRepository()


def format_price(price):
    return f"${price:,.0f}".replace(",", ".")


def menu():

    print("\n========================================")
    print("           CAJA KIOSCO")
    print("========================================")
    print("1. Listar productos")
    print("2. Agregar producto")
    print("3. Registrar venta")
    print("4. Reporte del día")
    print("5. Salir")
    print("========================================")


while True:

    menu()

    option = input("Selecciona una opción: ")

    # ========================================
    # LISTAR PRODUCTOS
    # ========================================

    if option == "1":

        products = product_repo.get_all_products()

        print("\n========================================")
        print("         LISTA DE PRODUCTOS")
        print("========================================")

        if not products:
            print("No hay productos cargados.")
            continue

        for product in products:

            print(
                f"ID: {product.id_producto:<3}"
                f" | {product.name:<15}"
                f" | Precio: {format_price(product.price):<12}"
                f" | Stock: {product.stock}"
            )

    # ========================================
    # AGREGAR PRODUCTO
    # ========================================

    elif option == "2":

        try:

            print("\n========================================")
            print("          AGREGAR PRODUCTO")
            print("========================================")

            name = input("Nombre del producto: ")

            price = float(
                input("Precio: ")
            )

            stock = int(
                input("Stock: ")
            )

            product = Product(
                name=name,
                price=price,
                stock=stock
            )

            product_repo.add_product(product)

            print("\n Producto agregado correctamente.")

            print(
                f"ID: {product.id_producto} | "
                f"{product.name} | "
                f"{format_price(product.price)} | "
                f"Stock: {product.stock}"
            )

        except ValueError as e:

            print(f"\n Error: {e}")

    # ========================================
    # REGISTRAR VENTA
    # ========================================

    elif option == "3":

        print("\n========================================")
        print("          REGISTRAR VENTA")
        print("========================================")
        

        sell = Sell()

        products = product_repo.get_all_products()

        print("\n--- PRODUCTOS DISPONIBLES ---")

        for product in products:

            print(
                f"ID: {product.id_producto:<3}"
                f" | {product.name:<15}"
                f" | Precio: {format_price(product.price):<12}"
                f" | Stock: {product.stock}"
            )

        while True:

            try:

                product_id = int(
                    input("\nIngrese ID del producto o presione 0 para salir: ")
                )

                if product_id == 0:
                    break

                product = product_repo.get_id_product(
                    product_id
                )

                if product is None:

                    print(" Producto no encontrado.")
                    continue

                quantity = int(
                    input("Cantidad: ")
                )

                sell.add_item(product, quantity)

                print(" Producto agregado a la venta.")

            except ValueError:

                print("Error: Debe ingresar un número válido.")

        if not sell.items:

            print("\n No se agregaron productos.")
            continue

        sale_repo.add_sale(sell)

        for item in sell.items:

            sell_item_repo.add_sell_item(
                item,
                sell.sell_id
            )

        print("\n========================================")
        print(
            f"VENTA #{sell.sell_id} - "
            f"{sell.date.replace('T', ' ')[:16]}"
        )
        print("========================================")

        for item in sell.items:

            print(
                f"{item.product.name:<15}"
                f"x{item.quantity:<3}"
                f"{format_price(item.subtotal)}"
            )

            new_stock = (
                item.product.stock - item.quantity
            )

            product_repo.update_stock(
                item.product.id_producto,
                new_stock
            )

        print("----------------------------------------")
        print(f"TOTAL: {format_price(sell.total)}")
        print("========================================")

    # ========================================
    # REPORTE DEL DÍA
    # ========================================

    elif option == "4":

        print("\n========================================")

        print(
            f"REPORTE DE CAJA — "
            f"{datetime.now().strftime('%Y-%m-%d')}"
        )

        print("========================================")

        sales = sale_repo.sales_of_day()

        if not sales:

            print("No hay ventas registradas hoy.")
            continue

        for row in sales:

            sale_id = row[0]
            date = row[1]
            sale_total = row[2]

            formatted_hour = (
                date.replace("T", " ")[11:16]
            )

            print(
                f"\nVenta #{sale_id} — "
                f"{formatted_hour}"
            )

            items = sell_item_repo.get_by_sell(
                sale_id
            )

            for item in items:

                print(
                    f"{item.product.name:<15}"
                    f"x{item.quantity:<3}"
                    f"{format_price(item.subtotal)}"
                )

            print(
                f"Subtotal: "
                f"{format_price(sale_total)}"
            )

        print("----------------------------------------")

        print(
            f"Total de ventas: {len(sales)}"
        )

        print(
            f"TOTAL RECAUDADO: "
            f"{format_price(sale_repo.total_revenue_today())}"
        )

        print("========================================")

    # ========================================
    # SALIR
    # ========================================

    elif option == "5":

        print("\n========================================")
        print("   Saliendo del sistema...")
        print("========================================")

        break

    # ========================================
    # OPCIÓN INVÁLIDA
    # ========================================

    else:

        print("\n Opción inválida.")
        print("Seleccione una opción del 1 al 5.")