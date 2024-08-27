#Ejercicio 2 Un colegio privado desea registrar la asistencia de sus estudiantes a las
#clases cada docente tiene su listado de los estudiantes en los cuáles se
#les ha solicitado colocar a la par de cada estudiante si ha asistido, si
#cuenta con permiso o tiene inasistencia con la fecha respectiva.
#Actualmente esto se maneja por unas hojas de papel impreso y se
#entregan al director al final del día; la escuela necesita agilizar este
#proceso.
# Si el estudiante tiene un permiso el director necesita la razón de
#dicha falta, ¿Cómo solventarías esta situación? Agrega tu
#propuesta al código.

from datetime import date

#Clase de registro y asistencia 
class RegistroAsistencia:
    def __init__(self, fecha, estado, razon_permiso=None):
        self.fecha = fecha
        self.estado = estado  # 'Asistió', 'Permiso', 'Inasistencia'
        self.razon_permiso = razon_permiso

    def __str__(self):
        if self.estado == 'Permiso':
            return f"{self.fecha}: {self.estado} - Razón: {self.razon_permiso}"
        return f"{self.fecha}: {self.estado}"
    
#Clase estudiante
class Estudiante:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.registros_asistencia = []

    def agregar_registro_asistencia(self, registro):
        self.registros_asistencia.append(registro)

    def mostrar_asistencia(self):
        print(f"Asistencia para {self.nombre} ({self.matricula}):")
        for registro in self.registros_asistencia:
            print(registro)

#Clase de docente
class Docente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = {}

    def agregar_estudiante(self, estudiante):
        self.estudiantes[estudiante.matricula] = estudiante

    def registrar_asistencia(self, matricula, estado, razon_permiso=None):
        if matricula in self.estudiantes:
            registro = RegistroAsistencia(date.today(), estado, razon_permiso)
            self.estudiantes[matricula].agregar_registro_asistencia(registro)
        else:
            print(f"Estudiante con matrícula {matricula} no encontrado.")

    def mostrar_asistencia(self):
        print(f"Registro de asistencia del docente {self.nombre}:")
        for estudiante in self.estudiantes.values():
            estudiante.mostrar_asistencia()

#Clase de director
class Director:
    def __init__(self):
        self.registros_dia = []

    def agregar_registro_docente(self, docente):
        self.registros_dia.append(docente)

    def revisar_asistencia(self):
        print("Revisión de asistencia por el Director:")
        for docente in self.registros_dia:
            docente.mostrar_asistencia()

def main():
    # Crear estudiantes
    estudiante1 = Estudiante("Erick Chávez", "SMTR152021")
    estudiante2 = Estudiante("Alfredo Carranza", "SMTR059023")

    # Crear un docente
    docente1 = Docente("Ingeniero. Willian")

    # Agregar estudiantes al docente
    docente1.agregar_estudiante(estudiante1)
    docente1.agregar_estudiante(estudiante2)

    # Registrar asistencia de alumnos
    docente1.registrar_asistencia("SMTR152021", "Asistió")
    docente1.registrar_asistencia("SMTR059023", "Permiso", "Dificultad de salud")

    # Mostrar asistencia del docente
    docente1.mostrar_asistencia()

    # Crear un director
    director = Director()
    director.agregar_registro_docente(docente1)

    # El director controla la asistencia de alumnos y docente 
    director.revisar_asistencia()

if __name__ == "__main__":
    main()

#-----COMENTARIO Y EXPLICACION DE SOLUCION-----
#En este codigo realizamos un programma con POO ya que lleva CLASS , ESTUDIANTE,DOCENTE,DIRECTOR Y DE REGISTRO Y ASISTENCIA
#este codigo le perimite al colegio llevar un resgrito de los estudantes y docentes de forma ordenada 
#t asi mismo le permite al director la informacion del docente y su asistencia como asi mismo una explicacion 
# en caso de inacistencia al igual con los estudiantes les muestra su imformacion como su codigo 
# su asistencia y su falta...