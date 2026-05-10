# proyecto Kiosco
def menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Eliminar producto")
    print("4. Registrar venta")
    print("5. Ver ventas")
    print("6. Salir")

def pedir_id():
    while True:
        try:
            id_producto = int(input("Ingrese ID del producto (0 para finalizar): "))
            return id_producto
        except ValueError:
            print("x ID inválido. Ingrese un número.")

def agregar_producto(inventario, contador_id):
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    inventario[contador_id] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    print(f"x Producto '{nombre}' agregado con ID {contador_id}.")
    return contador_id + 1

def mostrar_inventario(inventario):
    print("\n--- INVENTARIO ---")
    if not inventario:
        print("Inventario vacío.")
    else:
        for id_producto, datos in inventario.items():
            print(f"ID: {id_producto} | {datos['nombre']} - Precio: {datos['precio']} - Cantidad: {datos['cantidad']}")

def eliminar_producto(inventario):
    id_producto = pedir_id()
    if id_producto == 0:
        return
    if id_producto in inventario:
        eliminado = inventario[id_producto]["nombre"]
        del inventario[id_producto]
        print(f"x Producto '{eliminado}' eliminado.")
    else:
        print("x ID no encontrado en inventario.")

def registrar_venta(inventario, ventas):
    while True:
        id_producto = pedir_id()
        if id_producto == 0:
            break
        if id_producto in inventario:
            cantidad = int(input("Cantidad vendida: "))
            if cantidad <= inventario[id_producto]["cantidad"]:
                inventario[id_producto]["cantidad"] -= cantidad
                total = cantidad * inventario[id_producto]["precio"]
                ventas.append({"producto": inventario[id_producto]["nombre"], "cantidad": cantidad, "total": total})
                print(f"x Venta registrada: {cantidad} x {inventario[id_producto]['nombre']} = ${total}")
            else:
                print("x Stock insuficiente.")
        else:
            print("x ID no encontrado en inventario.")

def ver_ventas(ventas):
    print("\n--- VENTAS ---")
    if ventas:
        for venta in ventas:
            print(f"Producto: {venta['producto']} - Cantidad: {venta['cantidad']} - Total: ${venta['total']}")
    else:
        print("No hay ventas registradas.")

def main():
    inventario = {}
    ventas = []
    contador_id = 1  
    while True:
        menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            contador_id = agregar_producto(inventario, contador_id)
        elif opcion == "2":
            mostrar_inventario(inventario)
        elif opcion == "3":
            eliminar_producto(inventario)
        elif opcion == "4":
            registrar_venta(inventario, ventas)
        elif opcion == "5":
            ver_ventas(ventas)
        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("x Opción inválida.")

if __name__ == "__main__":
    main()
