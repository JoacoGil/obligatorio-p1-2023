from Equipo import Equipo
from Piloto import Piloto
from PilotoReserva import PilotoReserva
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
        while True:
            try:
                id = input("Ingrese cedula: ")
                if not id.isdigit() or len(id) != 8:
                    raise ValueError("La cédula debe contener exactamente 8 dígitos sin puntos ni guiones.")
                break
            except ValueError as e:
                print(e)
        nombre = input("Ingrese nombre: ")
        fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
        nacionalidad = input("Ingrese nacionalidad: ")
        while True:
            try:
                salario = float(input("Ingrese salario: "))
                break
            except ValueError:
                print("El salario debe ser un número.")
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
            while True:
                try:
                    score = float(input("Ingrese score: "))
                    break
                except ValueError:
                    print("El score debe ser un número.")
            while True:
                try:
                    numero_auto = int(input("Ingrese número de auto: "))
                    break
                except ValueError:
                    print("El número de auto debe ser un número entero.")
            empleado = Piloto(id, nombre, nacionalidad, fecha_nacimiento, salario, score, numero_auto, 0, False)
            

        elif cargo == "2":
            # Alta de piloto de reserva
            while True:
                try:
                    score = float(input("Ingrese score: "))
                    break
                except ValueError:
                    print("El score debe ser un número.")
            while True:
                try:
                    numero_auto = int(input("Ingrese número de auto: "))
                    break
                except ValueError:
                    print("El número de auto debe ser un número entero.")
            empleado = PilotoReserva(id, nombre, nacionalidad, fecha_nacimiento, salario, score, numero_auto, 0, False)

        elif cargo == "3":
            # Alta de mecánico
            while True:
                try:
                    score = float(input("Ingrese score: "))
                    break
                except ValueError:
                    print("El score debe ser un número.")
            empleado = Mecanico(id, nombre, nacionalidad, fecha_nacimiento, salario, score)

        elif cargo == "4":
            # Alta de jefe de equipo
            empleado = DirectorEquipo(id, nombre, nacionalidad, fecha_nacimiento, salario)

        if empleado:
            # Agregar el empleado a la lista de empleados
            self.empleados.append(empleado)
            print("Empleado ingresado correctamente.")

    def alta_auto(self):
        print("\n--- Alta de Auto ---")
        modelo = input("Ingrese modelo: ")
        while True:
            try:
                score = float(input("Ingrese score: "))
                break
            except ValueError:
                print("El score debe ser un número.")
        color = input("Ingrese color: ")
        
        nuevo_auto = Auto(modelo, score, color)
        self.autos.append(nuevo_auto)

        print(f"Auto creado: Modelo={nuevo_auto.modelo}, Score={nuevo_auto.score}, Color={nuevo_auto.color}")
        

    def alta_equipo(self):
        print("\n--- Alta de Equipo ---")

        nombre_equipo = input("Ingrese nombre del equipo: ")
        pais_equipo = input("Ingrese país del equipo: ")
        año_equipo = input("Ingrese año de creación del equipo: ")

        nuevo_equipo = Equipo(nombre_equipo, pais_equipo, año_equipo)
        
        print(" -- Asignar modelo de auto -- ")

        modelo_auto = input("Ingrese modelo de auto: ")

        # Buscar auto por modelo
        if modelo_auto not in [auto.modelo for auto in self.autos]:
            print("Ese modelo de auto no existe.")
            return
        
        # Asignar auto al equipo
        nuevo_equipo.asignar_auto(modelo_auto)

        # Asignar empleados al equipo
        print(" -- Asignar empleados al equipo -- ")

        ci_empleados = []
        cant_pilotos = 0
        cant_mecanicos = 0
        cant_directores = 0
        cant_pilotos_reserva = 0

        for i in range(12):
            cedula_empleado = input(f"Ingrese cédula del empleado {i+1}: ")
            # Buscar empleado por cedula
            empleado = [empleado for empleado in self.empleados if empleado.id == cedula_empleado]
            if not empleado:
                print("Ese empleado no existe.")
                return
            # Verificar que el empleado no haya sido asignado a este equipo
            if cedula_empleado in ci_empleados:
                print("Ese empleado ya está asignado a este equipo.")
                return
            ci_empleados.append(cedula_empleado)
            # Verificar que el empleado no haya sido asignado a otro equipo
            if not self.is_employee_available(cedula_empleado):
                print("Ese empleado ya está asignado a otro equipo.")
                return
            # Asignar empleado al equipo
            empleado = empleado[0]
            if isinstance(empleado, Piloto) and cant_pilotos < 2:
                nuevo_equipo.agregar_piloto_titular(empleado)
                cant_pilotos += 1
            elif isinstance(empleado, Mecanico) and cant_mecanicos < 8:
                nuevo_equipo.agregar_mecanico(empleado)
                cant_mecanicos += 1
            elif isinstance(empleado, DirectorEquipo) and cant_directores < 1:
                nuevo_equipo.asignar_director(empleado)
                cant_directores += 1
            elif isinstance(empleado, PilotoReserva) and cant_pilotos_reserva < 1:
                nuevo_equipo.agregar_piloto_reserva(empleado)
                cant_pilotos_reserva += 1

        self.equipos.append(nuevo_equipo)
        print(f"Equipo creado: Nombre={nuevo_equipo.nombre}, País={nuevo_equipo.pais}, Año de creación={nuevo_equipo.año_creacion}")

    def is_employee_available(self, employee_id):
                for team in self.equipos:
                    for employee in team.get_all_empleados():
                        if employee.get_id() == employee_id:
                            return False
                return True

    def simular_carrera(self):
        # Implementar la lógica para simular una carrera
        print("\n--- Simular Carrera ---")

        self.lesionados = []
        self.abandonan = []
        self.error_en_pits = []
        self.penalizados = []

        lesionados = input("Ingrese nro de auto de todos los pilotos lesionados: ").split(',')
        abandonan = input("Ingrese nro auto de todos los pilotos que abandonan separado por coma: ").split(',')
        error_en_pits = input("Ingrese nro de auto de todos los pilotos que comente error en pits: ").split(',')
        penalizados = input("Ingrese nro de auto de todos los pilotos que reciben penalidad: ").split(',')

    def realizar_consultas(self):
        # Implementar la lógica para realizar consultas
        print("\n--- Realizar Consultas ---")
        pass

# Función principal para ejecutar el programa
if __name__ == "__main__":
    programa = ProgramaF1()
    programa.ejecutar()
