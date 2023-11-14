from entities.Equipo import Equipo
from entities.Piloto import Piloto
from entities.PilotoReserva import PilotoReserva
from entities.Mecanico import Mecanico
from entities.DirectorEquipo import DirectorEquipo
from entities.Auto import Auto

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
                for employee in self.empleados:
                    if employee.get_id() == id:
                        raise ValueError("Ya existe un empleado con esa cédula.")
                break
                 
            except ValueError as e:
                print(e)
                return

        
        nombre = input("Ingrese nombre: ")
        fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
        nacionalidad = input("Ingrese nacionalidad: ")
        while True:
            try:
                salario = float(input("Ingrese salario: "))
                break
            except ValueError:
                print("El salario debe ser un número.")
                return
        # Validar y solicitar el tipo de empleado
        while True:
            print("Seleccione el cargo:")
            print("1. Piloto")
            print("2. Piloto de reserva")
            print("3. Mecánico")
            print("4. Director de equipo")
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
                    return
            while True:
                try:
                    numero_auto = int(input("Ingrese número de auto: "))
                    break
                except ValueError:
                    print("El número de auto debe ser un número entero.")
                    return
            empleado = Piloto(id, nombre, nacionalidad, fecha_nacimiento, salario, score, numero_auto, 0, False)
            

        elif cargo == "2":
            # Alta de piloto de reserva
            while True:
                try:
                    score = float(input("Ingrese score: "))
                    break
                except ValueError:
                    print("El score debe ser un número.")
                    return
            while True:
                try:
                    numero_auto = int(input("Ingrese número de auto: "))
                    break
                except ValueError:
                    print("El número de auto debe ser un número entero.")
                    return
            empleado = PilotoReserva(id, nombre, nacionalidad, fecha_nacimiento, salario, score, numero_auto, 0, False)

        elif cargo == "3":
            # Alta de mecánico
            while True:
                try:
                    score = float(input("Ingrese score: "))
                    break
                except ValueError:
                    print("El score debe ser un número.")
                    return
            empleado = Mecanico(id, nombre, nacionalidad, fecha_nacimiento, salario, score)

        elif cargo == "4":
            # Alta de Director de equipo
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
                return
            
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
        print("\n--- Simular Carrera ---")

        lesionados = input("Ingrese nro de auto de todos los pilotos lesionados (separados por coma): ")
        abandonan = input("Ingrese nro de auto de todos los pilotos que abandonan (separados por coma): ")
        error_en_pits = input("Ingrese nro de auto de los pilotos que cometen error en pits (separados por coma): ")
        penalizados = input("Ingrese nro de auto de los pilotos que reciben penalidad (separados por coma): ")

        # Obtener todos los pilotos titulares de todos los equipos
        pilotos_en_carrera = [piloto for equipo in self.equipos for piloto in equipo.get_pilotos_titulares()]

        # Remover pilotos lesionados
        for auto in lesionados.split(','):
            piloto_lesionado = next((piloto for piloto in pilotos_en_carrera if piloto.auto.numero == int(auto)), None)
            if piloto_lesionado in pilotos_en_carrera:
                pilotos_en_carrera.remove(piloto_lesionado)

        # Remover pilotos que abandonan
        for auto in abandonan.split(','):
            piloto_abandona = next((piloto for piloto in pilotos_en_carrera if piloto.auto.numero == int(auto)), None)
            if piloto_abandona in pilotos_en_carrera:
                pilotos_en_carrera.remove(piloto_abandona)

        # Calcular puntajes finales para los pilotos que siguen en carrera
        puntajes_finales = {}
        for piloto in pilotos_en_carrera:
            score_final = piloto.auto.score + piloto.score + sum(mecanico.score for mecanico in piloto.equipo.mecanicos)
            if str(piloto.auto.numero) in error_en_pits.split(','):
                score_final -= 5
            if str(piloto.auto.numero) in penalizados.split(','):
                score_final -= 8
            if piloto.auto.numero in [int(auto) for auto in abandonan.split(',')]:
                score_final = 0
            puntajes_finales[piloto] = score_final

        # Ordenar pilotos por puntaje final
        pilotos_ordenados = sorted(puntajes_finales, key=puntajes_finales.get, reverse=True)

        # Asignar puntos basados en el orden
        puntos = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
        for i, piloto in enumerate(pilotos_ordenados):
            if i < len(puntos):
                piloto.sumar_puntos(puntos[i])

        # Mostrar el orden de llegada
        print("\n--- Orden de llegada ---")
        for i, piloto in enumerate(pilotos_ordenados):
            print(f"{i + 1}. Piloto {piloto.nombre} del Equipo {piloto.equipo.nombre}")

        # Limpiar las lesiones al final de la carrera
        for equipo in self.equipos:
            equipo.curar_lesiones_pilotos()


    def realizar_consultas(self):
        # Implementar la lógica para realizar consultas
        print("\n--- Realizar Consultas ---")
        print("1. Top 10 pilotos con más puntos")
        print("2. Resumen de campeonato de constructores")
        print("3. Top 5 pilotos mejor pagados")
        print("4. Top 3 pilotos más habilidosos")
        print("5. Retornar jefes de equipo")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            self.top_10_pilotos_mas_puntos()
        elif opcion == "2":
            self.resumen_campeonato_constructores()
        elif opcion == "3":
            self.top_5_pilotos_mejor_pagados()
        elif opcion == "4":
            self.top_3_pilotos_mas_habilidosos()
        elif opcion == "5":
            self.retornar_jefes_de_equipo()
        else:
            print("Opción no válida.")
            return
        
    def top_10_pilotos_mas_puntos(self):
        pilotos = [pilot for team in self.equipos for pilot in team]
        pilotos_ordenados = sorted(pilotos, key=lambda piloto: piloto.puntaje_campeonato, reverse=True)
        return pilotos_ordenados[:10]
    
    def resumen_campeonato_constructores(self):
        resumen = {}
        for equipo in self.equipos:
            puntos_equipo = sum(piloto.puntaje_campeonato for piloto in equipo.pilotos_titulares + [equipo.piloto_reserva] if piloto)
            resumen[equipo.nombre] = puntos_equipo
        return dict(sorted(resumen.items(), key=lambda x: x[1], reverse=True))

    def top_5_pilotos_mejor_pagados(self):
        pilotos = [pilot for team in self.equipos for pilot in team]
        pilotos_ordenados = sorted(pilotos, key=lambda piloto: piloto.salario, reverse=True)

        return pilotos_ordenados[:5]

    def top_3_pilotos_mas_habilidosos(self):
        pilotos = [pilot for team in self.equipos for pilot in team]
        pilotos_ordenados = sorted(pilotos, key=lambda piloto: piloto.score, reverse=True)
        return pilotos_ordenados[:3]

    def retornar_jefes_de_equipo(self):
        jefes = [(equipo.director.nombre, equipo.nombre) for equipo in self.equipos]
        return sorted(jefes, key=lambda x: x[0])


# Función principal para ejecutar el programa
if __name__ == "__main__":
    programa = ProgramaF1()
    programa.ejecutar()
