from Equipo import Equipo
from Piloto import Piloto
from Mecanico import Mecanico
from DirectorEquipo import DirectorEquipo
from Auto import Auto

# # Ejemplo de uso:
# equipo1 = Equipo("Equipo A", "Argentina", "2010")
# piloto1 = Piloto("12345678", "Piloto 1", 30, "Nacionalidad 1", "01/01/1990", 50000, 80, 1, 100, False)
# mecanico1 = Mecanico("23456789", "Mecánico 1", 35, "Nacionalidad 2", "15/03/1985", 40000, 90)
# director1 = DirectorEquipo("34567890", "Director 1", 40, "Nacionalidad 3", "10/05/1980", 60000)
# auto1 = Auto("Modelo 1", 100, "Rojo")

# equipo1.agregar_piloto_titular(piloto1)
# equipo1.agregar_mecanico(mecanico1)
# equipo1.asignar_director(director1)
# equipo1.asignar_auto(auto1)

# # ------------------------------- Printear todas las propiedades del equipo 1 ---------------------------------------------------
# print("Nombre del equipo:", equipo1.nombre)
# print("País del equipo:", equipo1.pais)
# print("Año de creación del equipo:", equipo1.año_creacion)
# print("Pilotos titulares del equipo:")
# for piloto in equipo1.pilotos_titulares:
#     print("  - Nombre:", piloto.nombre)
#     print("    ID:", piloto.id)
#     print("    Edad:", piloto.edad)
#     print("    Nacionalidad:", piloto.nacionalidad)
#     print("    Fecha de nacimiento:", piloto.fecha_nacimiento)
#     print("    Salario:", piloto.salario)
#     print("    Score:", piloto.score)
#     print("    Número de auto:", piloto.numero_auto)
#     print("    Puntaje de campeonato:", piloto.puntaje_campeonato)
#     print("    Lesionado:", piloto.lesionado)
# if equipo1.piloto_reserva:
#     print("Piloto reserva del equipo:")
#     print("  - Nombre:", equipo1.piloto_reserva.nombre)
#     print("    ID:", equipo1.piloto_reserva.id)
#     print("    Edad:", equipo1.piloto_reserva.edad)
#     print("    Nacionalidad:", equipo1.piloto_reserva.nacionalidad)
#     print("    Fecha de nacimiento:", equipo1.piloto_reserva.fecha_nacimiento)
#     print("    Salario:", equipo1.piloto_reserva.salario)
#     print("    Score:", equipo1.piloto_reserva.score)
#     print("    Número de auto:", equipo1.piloto_reserva.numero_auto)
#     print("    Puntaje de campeonato:", equipo1.piloto_reserva.puntaje_campeonato)
#     print("    Lesionado:", equipo1.piloto_reserva.lesionado)
# print("Mecánicos del equipo:")
# for mecanico in equipo1.mecanicos:
#     print("  - Nombre:", mecanico.nombre)
#     print("    ID:", mecanico.id)
#     print("    Edad:", mecanico.edad)
#     print("    Nacionalidad:", mecanico.nacionalidad)
#     print("    Fecha de nacimiento:", mecanico.fecha_nacimiento)
#     print("    Salario:", mecanico.salario)
#     print("    Score:", mecanico.score)
# if equipo1.director:
#     print("Director del equipo:")
#     print("  - Nombre:", equipo1.director.nombre)
#     print("    ID:", equipo1.director.id)
#     print("    Edad:", equipo1.director.edad)
#     print("    Nacionalidad:", equipo1.director.nacionalidad)
#     print("    Fecha de nacimiento:", equipo1.director.fecha_nacimiento)
#     print("    Salario:", equipo1.director.salario)
# if equipo1.auto:
#     print("Auto del equipo:")
#     print("  - Modelo:", equipo1.auto.modelo)
#     print("    Score:", equipo1.auto.score)
#     print("    Color:", equipo1.auto.color)
# # ----------------------------------------------------------------------------------


# Clase Principal del Programa
class ProgramaF1:
    def __init__(self):
        self.empleados = []
        self.autos = []
        self.equipos = []

    def ejecutar(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Alta de empleado")
            print("2. Alta de auto")
            print("3. Alta de equipo")
            print("4. Simular carrera")
            print("5. Realizar consultas")
            print("6. Finalizar programa")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.alta_empleado()
            elif opcion == "2":
                self.alta_auto()
            elif opcion == "3":
                self.alta_equipo()
            elif opcion == "4":
                self.simular_carrera()
            elif opcion == "5":
                self.realizar_consultas()
            elif opcion == "6":
                print("Programa finalizado.")
                break
            else:
                print("Opción no válida. Por favor, elija una opción válida.")

    def alta_empleado(self):
        print("\n--- Alta de Empleado ---")

        # Solicitar datos generales del empleado
        id = input("Ingrese cedula: ")
        if not id.isdigit() or len(id) != 8:
                    raise ValueError("La cédula debe contener exactamente 8 dígitos sin puntos ni guiones.")
        nombre = input("Ingrese nombre: ")
        edad = int(input("Ingrese edad: "))
        fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
        nacionalidad = input("Ingrese nacionalidad: ")
        salario = float(input("Ingrese salario: "))

        # Validar y solicitar el tipo de empleado
        while True:
            print("Seleccione el cargo:")
            print("1. Piloto")
            print("2. Piloto de reserva")
            print("3. Mecánico")
            print("4. Jefe de equipo")
            cargo = input("Opción: ")

            if cargo in ["1", "2", "3", "4"]:
                break
            else:
                print("Opción no válida. Por favor, elija una opción válida.")

        if cargo == "1":
            # Alta de piloto
            score = float(input("Ingrese score: "))
            numero_auto = int(input("Ingrese número de auto: "))
            empleado = Piloto(id, nombre, edad, nacionalidad, fecha_nacimiento, salario, score, numero_auto, 0, False)
            

        elif cargo == "2":
            # Alta de piloto de reserva
            score = float(input("Ingrese score: "))
            numero_auto = int(input("Ingrese número de auto: "))
            empleado = Piloto(id, nombre, edad, nacionalidad, fecha_nacimiento, salario, score, numero_auto, 0, False)

        elif cargo == "3":
            # Alta de mecánico
            score = float(input("Ingrese score: "))
            empleado = Mecanico(id, nombre, edad, nacionalidad, fecha_nacimiento, salario, score)

        elif cargo == "4":
            # Alta de jefe de equipo
            empleado = DirectorEquipo(id, nombre, edad, nacionalidad, fecha_nacimiento, salario)

        if empleado:
            # Agregar el empleado a la lista de empleados
            self.empleados.append(empleado)
            print("Empleado ingresado correctamente.")

    def alta_auto(self):
        # Implementar la lógica para dar de alta un auto
        pass

    def alta_equipo(self):
        # Implementar la lógica para dar de alta un equipo
        pass

    def simular_carrera(self):
        # Implementar la lógica para simular una carrera
        pass

    def realizar_consultas(self):
        # Implementar la lógica para realizar consultas
        pass

# Función principal para ejecutar el programa
if __name__ == "__main__":
    programa = ProgramaF1()
    programa.ejecutar()


