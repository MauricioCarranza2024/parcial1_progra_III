"""
Una empresa cuenta con dos tipos de empleados: aquellos con plaza fija y aquellos que trabajan por horas.
Se han registrado los datos de ambos tipos y, al generar la planilla de pago, se realizan dos cálculos diferentes.
A los empleados de plaza fija se les paga el salario base más comisiones, mientras que a los empleados por horas
se les paga en función de la cantidad de horas trabajadas.

Adicionalmente, si un empleado ha laborado más de 5 años, sin importar su tipo de contrato, se le otorga un bono adicional.
"""

#en esta primer clase es la que representa un empleado generico
class Empleado:
    def __init__(self, nombre, años_trabajados):
        self.nombre = nombre
        self.años_trabajados = años_trabajados

    def calcular_bono(self):
        return 200 if self.años_trabajados > 5 else 0

    def calcular_pago(self):
        pass

#esta clase es la que representa a un empleado con plaza fija
class EmpleadoPlazaFija(Empleado):
    def __init__(self, nombre, años_trabajados, salario_base, comisiones):
        super().__init__(nombre, años_trabajados)
        self.salario_base = salario_base
        self.comisiones = comisiones

    def calcular_pago(self):
        salario_total = self.salario_base + self.comisiones + self.calcular_bono()
        return salario_total

#esta clase es la que representa a un empleado que trabaja por horas
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, años_trabajados, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre, años_trabajados)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_pago(self):
        salario_total = (self.horas_trabajadas * self.tarifa_por_hora) + self.calcular_bono()
        return salario_total

#esta clase la hago para gestionar la planilla de empleados y tambien hice una para almacenar los empleados
class Empresa:
    def __init__(self):
        self.empleados = []  

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def generar_planilla(self):
        print("\nGenerando planilla de pago...")
        for empleado in self.empleados:
            pago = empleado.calcular_pago()
            print(f"Empleado: {empleado.nombre}, Pago Total: ${pago:.2f}")

#en esta funcion es la principal que hace que se ejecute el programa
def main():
    empresa = Empresa()  
    while True:
        print("\nAgregar nuevo empleado:")
        tipo_empleado = input("¿Es empleado de Plaza Fija (f) o por Horas (h)? (f/h): ").lower()

        nombre = input("Ingrese el nombre del empleado: ")
        años_trabajados = int(input("Ingrese los años trabajados: "))

        if tipo_empleado == 'f':
            salario_base = float(input("Ingrese el salario base: "))
            comisiones = float(input("Ingrese las comisiones: "))
            empleado = EmpleadoPlazaFija(nombre, años_trabajados, salario_base, comisiones)

        elif tipo_empleado == 'h':
            horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
            tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))
            empleado = EmpleadoPorHoras(nombre, años_trabajados, horas_trabajadas, tarifa_por_hora)

        else:
            print("Tipo de empleado no válido. Intente nuevamente.")
            continue

        #aqui agregue el empleado a lista
        empresa.agregar_empleado(empleado)  
        continuar = input("¿Desea agregar otro empleado? (s/n): ").lower()
        if continuar != 's':
            break

    empresa.generar_planilla()


if __name__ == "__main__":
    main()
