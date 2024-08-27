#Ejercicio 1 Una tienda local vende diversos productos, cada vez que un cliente
#hace una compra niña mary se encarga de anotarlo en una libreta. A su
#vez, con una calculadora le da el total a cada cliente y les da su
#respectivo vuelto en caso de necesitarlo.
# Niña mary también se encarga de atender a los proveedores que
#le dan cierta cantidad de producto y un precio sugerido de venta,
#propón una solución dentro de tu programa para ayudarle.

import csv

# M1ostrar el inventario
def mostrar_inventario(inventario):
    print("Inventario de la tienda:")
    for producto, datos in inventario.items():
        print(f"{producto}: {datos['cantidad']} unidades, Precio: {datos['precio_venta']}")

# Registrar ventas 
def registrar_venta(inventario):
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad vendida: "))
    
    if producto in inventario and inventario[producto]['cantidad'] >= cantidad:
        total = cantidad * inventario[producto]['precio_venta']
        print(f"El total a pagar es: {total}")
        pago = float(input("Ingrese el monto con el que paga el cliente: "))
        vuelto = pago - total
        print(f"El vuelto para el cliente es: {vuelto}")
        
        inventario[producto]['cantidad'] -= cantidad
        print(f"Venta registrada. Quedan {inventario[producto]['cantidad']} unidades de {producto}.")
    else:
        print("No hay suficiente stock o el producto no existe en el inventario.")

# Función para registrar un nuevo producto
def registrar_recepcion(inventario):
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad recibida: "))
    precio_compra = float(input("Ingrese el precio de compra del producto: "))
    precio_venta = float(input("Ingrese el precio de venta sugerido: "))
    
    if producto in inventario:
        inventario[producto]['cantidad'] += cantidad
        inventario[producto]['precio_compra'] = precio_compra
        inventario[producto]['precio_venta'] = precio_venta
    else:
        inventario[producto] = {'cantidad': cantidad, 'precio_compra': precio_compra, 'precio_venta': precio_venta}
    
    print(f"Producto {producto} registrado/actualizado en el inventario.")


def main():
    inventario = {}
    
    while True:
        print("\n1. Registrar Venta")
        print("\n2. Registrar Recepción de Producto")
        print("\n3. Mostrar Inventario")
        print("\n4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_venta(inventario)
        elif opcion == '2':
            registrar_recepcion(inventario)
        elif opcion == '3':
            mostrar_inventario(inventario)
        elif opcion == '4':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
#-----COMENTARIO Y EXPLICACION DE SOLUCION-----
#En este codigo la solucion que se dio fue que a niña Mary se le facilite almacenar el inventario
#como asi mismo llevar el control de registro y los precios ya que eso le facilita a niña Mary a llevar 
#una actualizacion y control de precios y productos de forma mas ordenada, en este caso no utilizamos POO porque es una enfoque procimental
# porque las funciones y datos estan separados...