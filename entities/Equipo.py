class Equipo:
    def __init__(self, nombre, pais, año_creacion):
        self.nombre = nombre
        self.pais = pais
        self.año_creacion = año_creacion
        self.pilotos_titulares = []
        self.piloto_reserva = None
        self.mecanicos = []
        self.director = None
        self.auto = None

    def agregar_piloto_titular(self, piloto):
        self.pilotos_titulares.append(piloto)

    def agregar_piloto_reserva(self, pilotoReserva):
        self.piloto_reserva = pilotoReserva

    def agregar_mecanico(self, mecanico):
        self.mecanicos.append(mecanico)

    def asignar_director(self, director):
        self.director = director

    def asignar_auto(self, auto):
        self.auto = auto

    def get_all_empleados(self):
        empleados = []
        empleados.append(self.director)
        empleados.extend(self.pilotos_titulares)
        empleados.append(self.piloto_reserva)
        empleados.extend(self.mecanicos)
        return empleados