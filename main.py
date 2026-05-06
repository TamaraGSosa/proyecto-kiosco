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
     # 👇 MODIFICACIÓN 1: Inicializar un contador para los IDs de ventas.
     # En un sistema real, este ID se cargaría del último ID en la base de datos
     # para asegurar continuidad, pero para este ejemplo, es suficiente.
     next_sale_id = 1 
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
                 
                 # ✅ CORRECCIÓN ANTERIOR: Guardar el producto en el repositorio
                 product_repo.insertar_producto(producto) 
                 
                 print(f"Producto {producto.name} agregado correctamente.")
             except ValueError:
                 print("Error: El precio y el stock deben ser números válidos.")
             except Exception as e:
                 print(f"Error inesperado al agregar producto: {e}")
         elif opcion == "2":
             try:
                 productos = product_repo.listar_productos()  # Este método debe devolver una lista de Product
                 if not productos:
                     print("No hay productos cargados en el sistema.")
                 else:
                     print("\n--- Listado de Productos ---")
                     for p in productos:
                         print(f"ID: {p.id_producto} - {p.name} - ${p.price:.2f} - Stock: {p.stock}") # Asumo que Product tiene id_producto
             except Exception as e:
                 print(f"Error al listar productos: {e}")
         elif opcion == "3":
              try:
                  cliente_nombre = input("Nombre del cliente: ")
                  # 👇 MODIFICACIÓN 1: Pasar el ID único a la venta y actualizar el contador
                  venta = Sell(sale_id=next_sale_id, cliente=cliente_nombre) 
                  next_sale_id += 1 
                  
                  productos_disponibles = product_repo.listar_productos() # Cargar productos una vez para mostrar
                  if not productos_disponibles:
                      print("No hay productos disponibles para la venta. Cargue productos primero.")
                      continue # Vuelve al menú principal
                  comprando = True
                  while comprando: # 👇 MODIFICACIÓN 2: Bucle para agregar varios productos
                      print("\n--- Seleccione productos para la venta ---")
                      for idx, p in enumerate(productos_disponibles, start=1):
                          print(f"{idx}. {p.name} - ${p.price:.2f} - Stock: {p.stock}")
                      
                      seleccion_str = input("Ingrese el número del producto a agregar (0 para finalizar): ")
                      if seleccion_str == "0":
                          comprando = False
                          continue # Termina el bucle de agregar items
                          
                      try:
                          seleccion_idx = int(seleccion_str)
                          if not (1 <= seleccion_idx <= len(productos_disponibles)):
                              print("Número de producto inválido. Intente de nuevo.")
                              continue
                          
                          producto_elegido = productos_disponibles[seleccion_idx - 1]
                          
                          cantidad = int(input(f"Cantidad de '{producto_elegido.name}' (Stock: {producto_elegido.stock}): "))
                          if cantidad <= 0:
                              print("La cantidad debe ser mayor a cero.")
                              continue
                          
                          # ✅ Esto delega la lógica de agregar item, validar stock y actualizar stock en la DB a la clase Sell
                          # Por lo tanto, Sell.add_item DEBE hacer:
                          # 1. Validar stock
                          # 2. Crear SaleDetail y agregarlo a la venta
                          # 3. Llamar a product_repo.actualizar_stock(producto_elegido.id_producto, producto_elegido.stock - cantidad)
                          venta.add_item(producto_elegido, cantidad, product_repo) 
                          
                          print(f"'{cantidad}' de '{producto_elegido.name}' agregado a la venta.")
                          
                      except ValueError:
                          print("Entrada inválida. Asegúrese de ingresar números.")
                      except Exception as e:
                          print(f"Error al agregar producto a la venta: {e}")
                  
                  # Después de que el cliente terminó de agregar productos
                  if not venta._items: # Asumo que Sell guarda los items en una lista llamada _items
                      print("Venta cancelada o sin productos. Volviendo al menú principal.")
                      continue # Si no se agregó nada, no se guarda la venta
                      
                  print("\n--- Resumen de Venta ---")
                  # Aquí puedes agregar un bucle para imprimir cada SaleDetail de venta._items
                  for item in venta._items:
                      print(f"- {item.quantity} x {item.product.name} (${item.product.price:.2f} c/u) = ${item.subtotal:.2f}")
                  print(f"TOTAL A PAGAR: ${venta.total:.2f}")
                  
                  # ✅ CORRECCIÓN ANTERIOR: Guardar la venta en el repositorio
                  sell_repo.insertar_venta(venta) 
                  print(f"Venta ID {venta.sale_id} para {cliente_nombre} guardada correctamente.")
                  
              except ValueError:
                  print("Error en la entrada de datos. Por favor, intente de nuevo con valores válidos.")
              except Exception as e:
                  print(f"Error inesperado al realizar la venta: {e}")
                  
         elif opcion == "4":
             print("Saliendo del sistema...")
             break
         else:
             print("Opción inválida, intente nuevamente.")
if __name__ == "__main__":
     main()
