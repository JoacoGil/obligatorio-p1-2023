from entities.Empleado import Empleado

class Mecanico(Empleado):
    def __init__(self, id, nombre, nacionalidad, fecha_nacimiento, salario, score):
        super().__init__(id, nombre, nacionalidad, fecha_nacimiento, salario)
        self.score = score