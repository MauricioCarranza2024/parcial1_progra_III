"""
Un hotel de playa cuenta con un recepcionista que se encarga de
presentar a los clientes las opciones de habitaciones disponibles junto
con sus precios. Tras la elección de la habitación, el recepcionista
solicita los datos personales del cliente y el número de noches que
permanecerá en el hotel. Finalmente, entrega al cliente una factura
detallada con el total de los gastos.

Adicionalmente, los clientes pueden solicitar servicios extra,
como el uso de la piscina o la cancha de golf, que tienen un costo
adicional. Implementa esta funcionalidad en tu programa.
"""

# Clase que representa una habitación del hotel
class Habitacion:
    def __init__(self, tipo, precio):
        self.tipo = tipo
        self.precio = precio

# Clase que representa a un cliente con sus datos personales y servicios extras seleccionados
class Cliente:
    def __init__(self, nombre, apellido, tel, noches):
        self.nombre = nombre
        self.apellido = apellido
        self.tel = tel
        self.noches = noches
        self.servicios_extras = []  # Lista para almacenar los servicios extras seleccionados por el cliente
        self.costo_total = 0  # Costo total que se calculará más adelante

# Clase que representa un servicio extra del hotel
class ServicioExtra:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Clase que representa el hotel y contiene la lógica para manejar habitaciones y servicios extras
class Hotel:
    def __init__(self):
        self.habitaciones = [
            Habitacion("Estándar", 50),
            Habitacion("Suite", 100),
            Habitacion("Deluxe", 150)
        ]
        self.servicios_extras = [
            ServicioExtra("Piscina", 20),
            ServicioExtra("Cancha de Golf", 50)
        ]

    # este metodo para mostrar las habitaciones disponibles
    def mostrar_habitaciones(self):
        print("Opciones de habitaciones disponibles:")
        for idx, habitacion in enumerate(self.habitaciones):
            print(f"{idx + 1}. {habitacion.tipo} - ${habitacion.precio} por noche")

    # este metodo para mostrar los servicios extras disponibles
    def mostrar_servicios_extras(self):
        print("Opciones de servicios extra disponibles:")
        for idx, servicio in enumerate(self.servicios_extras):
            print(f"{idx + 1}. {servicio.nombre} - ${servicio.precio}")

    # este metodo es para generar y mostrar la factura detallada para el cliente
    def generar_factura(self, cliente, habitacion):
        costo_habitacion = habitacion.precio * cliente.noches
        costo_servicios = sum(servicio.precio for servicio in cliente.servicios_extras)
        cliente.costo_total = costo_habitacion + costo_servicios

        print("\n--- Factura ---")
        print(f"Cliente: {cliente.nombre} {cliente.apellido}")
        print(f"Telefono: {cliente.tel}")
        print(f"Habitación: {habitacion.tipo} - ${habitacion.precio} por noche")
        print(f"Noches: {cliente.noches}")
        print(f"Costo de la habitación: ${costo_habitacion} \n")
        if cliente.servicios_extras:
            print("---Servicios Extra que el cliente agrego---")
            for servicio in cliente.servicios_extras:
                print(f"- {servicio.nombre}: ${servicio.precio}")
        print(f"Costo total servicios extra: ${costo_servicios}")
        print(f"Total a pagar: ${cliente.costo_total}")
        print("------------------------------------------------\n")

# Función principal que ejecuta el flujo del programa
def main():
    hotel = Hotel()  # Crea una instancia del hotel
    
    hotel.mostrar_habitaciones()
    
    opcion_habitacion = int(input("Seleccione una habitación (1-3): ")) - 1
    habitacion_elegida = hotel.habitaciones[opcion_habitacion]

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    tel = input("Ingrese su numero de telefono: ")
    noches = int(input("Ingrese el número de noches que permanecerá en el hotel: "))

    cliente = Cliente(nombre, apellido, tel, noches)  # Crea una instancia del cliente

    hotel.mostrar_servicios_extras()

    while True:
        agregar_servicio = input("¿Desea agregar un servicio extra? (s/n): ").lower()
        if agregar_servicio == 's':
            opcion_servicio = int(input("Seleccione un servicio extra (1-2): ")) - 1
            servicio_elegido = hotel.servicios_extras[opcion_servicio]
            cliente.servicios_extras.append(servicio_elegido)
        else:
            break

    hotel.generar_factura(cliente, habitacion_elegida)

# Punto de entrada del programa
if __name__ == "__main__":
    main()