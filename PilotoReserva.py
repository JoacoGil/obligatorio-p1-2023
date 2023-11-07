from Piloto import Piloto

class PilotoReserva(Piloto):
    def __init__(self, id, nombre, nacionalidad, fecha_nacimiento, salario, score, numero_auto, puntaje_campeonato, lesionado):
        super().__init__(id, nombre, nacionalidad, fecha_nacimiento, salario, score, numero_auto, puntaje_campeonato, lesionado)